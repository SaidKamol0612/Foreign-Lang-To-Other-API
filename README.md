# 🎧 Foreign-Lang-To-Other Audio Transcriber & Translator

A project that automatically transcribes audio from a video URL from YouTube and translates the text from foreign languages to other.

## 🚀 Features

- 🔗 Download audio from a given URL (e.g., YouTube)
- 🎙️ Convert and split audio into chunks
- 🧠 Transcribe audio using `faster-whisper`
- 🌐 Translate transcribed text into other languages using Google Translate
- 🧹 Automatically clean up created files after processing

---

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — web framework
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — video/audio downloader from URLs (YouTube and others)
- [ffmpeg](https://ffmpeg.org/) — audio/video processing
- [pydub](https://github.com/jiaaro/pydub) — audio processing and chunking
- [faster-whisper](https://github.com/guillaumekln/faster-whisper) — fast Whisper model for transcription
- [googletrans](https://pypi.org/project/googletrans/) — text translation

---

## 📦 Installation

```bash
git clone https://github.com/your-username/en-or-ru-to-uz-transcriber.git
cd en-or-ru-to-uz-transcriber

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # for Linux/Mac
.venv\Scripts\activate      # for Windows

# Install dependencies
pip install -r requirements.txt
```
