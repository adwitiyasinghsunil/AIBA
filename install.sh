#!/bin/bash

echo "----------------------------------------------------------------"
echo "   AIBA (Artificial Intelligence Behavioural Analysis) Setup    "
echo "----------------------------------------------------------------"

# 1. System Dependencies (Linux only - for PyAudio)
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "[*] Detected Linux System. Checking system dependencies..."
    if command -v apt-get &> /dev/null; then
        echo "    Installing PortAudio (required for microphone)..."
        sudo apt-get update && sudo apt-get install -y python3-pyaudio portaudio19-dev
    else
        echo "    [!] Warning: Non-Debian Linux detected. Ensure 'portaudio' is installed manually."
    fi
fi

# 2. Python Dependencies
echo "[*] Installing Python Modules..."
pip install --upgrade pip
pip install rich opencv-python numpy pyautogui pyaudio SpeechRecognition transformers torch hf_xet

echo "----------------------------------------------------------------"
echo "   [✓] Installation Complete. Run with: python AIBA_System.py   "
echo "----------------------------------------------------------------"
