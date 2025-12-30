# AIBA (Artificial Intelligence Behavioural Analysis)

> **v1.0** | *Multimodal Intelligence System*

AIBA is an advanced Python-based behavioral analysis tool designed to process and interpret multimodal data streams. It integrates Natural Language Processing (NLP), Computer Vision, and Audio Recognition to provide real-time summaries and insights from user interactions.

## 🚀 Features

* **🧠 Neural Summarization Core:** Utilizes the `bart-large-cnn` transformer model to analyze complex text blocks and extract behavioral intent.
* **🎤 Acoustic Analysis:** Real-time speech-to-text transcription followed by immediate semantic analysis.
* **👁️ Visual Monitoring:** Captures screen activity and generates visual stream reports for behavioral context (includes localized recording).
* **💾 Short-Term Memory:** "Train" the system on the fly by feeding it raw data, which is stored in temporary memory nodes for subsequent analysis.
* **✨ Aesthetic UI:** Features a futuristic, CLI-based interface using the `Rich` library.

## 🛠️ Installation

Ensure you have Python 3.8+ installed.

### 1. Clone the Repository
```bash
git clone https://github.com/adwitiyasinghsunil/AIBA.git
cd AIBA

then run this----


#on windows only

pip install --upgrade pip
pip install rich opencv-python numpy pyautogui pyaudio SpeechRecognition transformers torch hf_xet




#on linux only(for audio recognition failures)----



if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo apt-get update && sudo apt-get install -y python3-pyaudio portaudio19-dev
fi
