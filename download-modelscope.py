import os
from modelscope.hub.snapshot_download import snapshot_download

# 设置缓存路径
os.environ['MODELSCOPE_CACHE'] = './checkpoints'

# 要下载的模型列表
models = [
    'stepfun-ai/Step-Audio-Tokenizer',
    'stepfun-ai/Step-Audio-Chat',
    'stepfun-ai/Step-Audio-TTS-3B'
]

# 下载每个模型
for model_id in models:
    print(f"正在下载模型：{model_id}")
    snapshot_download(model_id=model_id, cache_dir='./checkpoints')
print("✅ 所有模型下载完成")
