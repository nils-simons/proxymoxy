@echo off
pip install pyinstaller
pyinstaller --onefile -i icon.ico proxymoxy.py
PAUSE