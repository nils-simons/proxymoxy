@echo off
pip install pyinstaller
pyinstaller --onefile -i 256x256.ico proxymoxy.py
PAUSE