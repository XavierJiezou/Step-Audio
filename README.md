# Step-Audio Server for UltraEval-Audio

This is the server for the UltraEval-Audio project.

## Setup

```shell
git clone https://github.com/XavierJiezou/Step-Audio.git
cd Step-Audio
conda create -n step-audio python=3.11.7 -y
conda activate step-audio
pip install -r requirements.txt
```

## Download Models

```shell
python download-modelscope.py
```

## Run
```shell
CUDA_VISIBLE_DEVICES=4 HF_HOME=./checkpoints MODELSCOPE_CACHE=./checkpoints python adv_api.py \
  --tokenizer_path ./checkpoints/stepfun-ai/Step-Audio-Tokenizer \
  --tts_path ./checkpoints/stepfun-ai/Step-Audio-TTS-3B \
  --llm_path ./checkpoints/stepfun-ai/Step-Audio-Chat
```

Now, you can use `--model step-voice` in the UltraEval-Audio.
