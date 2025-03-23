import json
import base64
import io
import torchaudio

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from stepaudio import StepAudio
import tempfile
app = FastAPI()



def gen(inputs):
    response_text, response_audio, sr = model(inputs, "Tingting")
    audio_buffer = io.BytesIO()
    torchaudio.save(audio_buffer, response_audio, sr, format='wav')
    audio_base64 = base64.b64encode(audio_buffer.getvalue()).decode('utf-8')

    for i in range(0, len(audio_base64), 100):
        chunk = json.dumps({
            "text": response_text[i: i + 100],
            "audio": audio_base64[i: i + 100]
        }).encode()
        yield chunk+b'\0'


@app.post("/inference")
async def inference(request: Request):
    data = await request.json()
    audio_base64 = data.get("audio")
    audio_format = data.get('audio_format')
    text = data.get("text")

    if not audio_base64 and not text:
        return {"error": "Either 'audio' or 'text' must be provided."}

    # 构建输入
    inputs = []
    if text:
        inputs.append({"role": "system", "content": text})

    if audio_format and audio_base64:
        with tempfile.NamedTemporaryFile(suffix='.'+audio_format, delete=False) as f:
            f.write(base64.b64decode(audio_base64))
            audio_input = {"type": "audio", "audio": f.name}
            inputs.append({"role": "user", "content": audio_input})
            generator = gen(inputs)
            return StreamingResponse(generator)

    generator = gen(inputs)
    return StreamingResponse(generator)


if __name__ == "__main__":
    import uvicorn

    parser = argparse.ArgumentParser()
    parser.add_argument("--tokenizer_path", type=str, default="stepfun-ai/Step-Audio-Tokenizer")
    parser.add_argument("--tts_path", type=str, default="stepfun-ai/Step-Audio-TTS-3B")
    parser.add_argument("--llm_path", type=str, default="stepfun-ai/Step-Audio-Chat")
    args = parser.parse_args()

    # 初始化模型
    model = StepAudio(
        tokenizer_path=args.tokenizer_path,
        tts_path=args.tts_path,
        llm_path=args.llm_path,
    )

    uvicorn.run(app, host="0.0.0.0", port=5000)
