import os
os.system(f"pip install -q https://github.com/camenduru/stable-diffusion-webui-colab/releases/download/0.0.15/xformers-0.0.15.dev0+1515f77.d20221130-cp38-cp38-linux_x86_64.whl")
os.system(f"git clone https://github.com/camenduru/stable-diffusion-webui /home/user/app/stable-diffusion-webui")
os.system(f"wget -q https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/Anything-V3.0-pruned.ckpt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/Anything-V3.0-pruned.ckpt")
os.system(f"wget -q https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/Anything-V3.0.vae.pt -O /home/user/app/stable-diffusion-webui/models/Stable-diffusion/Anything-V3.0-pruned.vae.pt")
os.chdir("/home/user/app/stable-diffusion-webui")
# ----------------------------Duplicate this space and delete this block for Checkpoint Merger, Train, Settings, Extensions Tabs---------------------
os.system(f"sed -i -e '/(modelmerger_interface, \"Checkpoint Merger\", \"modelmerger\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
os.system(f"sed -i -e '/(train_interface, \"Train\", \"ti\"),/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
os.system(f"sed -i -e '/settings_interface, \"Settings\", \"settings\"/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
os.system(f"sed -i -e '/extensions_interface, \"Extensions\", \"extensions\"/d' /home/user/app/stable-diffusion-webui/modules/ui.py")
# ---------------------------------------------------------------------------------------------------------------------------------------------------
os.system(f"python launch.py --force-enable-xformers --disable-console-progressbars --enable-console-prompts --cors-allow-origins --cors-allow-origins-regex --gradio-debug --ui-config-file /home/user/app/ui-config.json --ui-settings-file /home/user/app/config.json")
