# Step-Audio Server for UltraEval-Audio

This is the server for the UltraEval-Audio project.


# Setup

```shell
git clone https://github.com/UltraEval/Step-Audio.git
cd Step-Audio
conda create -n env python=3.10 -y
conda activate env
pip install -r requirments.txt
```

# Run
```shell
python adv_api.py
```

Now, you can use `--model step-voice` in the UltraEval-Audio.