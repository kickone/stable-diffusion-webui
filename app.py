import os

os.system(f"python --version")
os.system(f"pip show gradio")
os.system(f"uname -r")
os.system(f"nvidia-smi")
os.system(f"pwd")

os.system(f"pip install -q https://github.com/camenduru/stable-diffusion-webui-colab/releases/download/0.0.15/xformers-0.0.15.dev0+1515f77.d20221130-cp38-cp38-linux_x86_64.whl")
os.system(f"git clone https://github.com/camenduru/stable-diffusion-webui /home/user/app/stable-diffusion-webui")
os.system(f"wget -q https://huggingface.co/camenduru/sd14/resolve/main/sd-v1-4.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/sd-v1-4.ckpt")
os.chdir("/home/user/app/stable-diffusion-webui")
os.system(f"pwd")
os.system(f"python launch.py --force-enable-xformers")

