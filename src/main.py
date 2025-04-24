from fastapi import FastAPI
import os
import uvicorn
from api import (
    download_video,
    convert_to_mp3,
    transcribe_audio,
    translate_text,
    VideoInput,
    AudioInput,
    TextInput,
)
from core import collect_data

TEMP_DIR = "temp_files"

if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

app = FastAPI(
    title="Working with foreign materials to Uzbek translation",
    description="This is a simple API for translating English and Russian materials to Uzbek.",
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to API for working with English / Russian materials to Uzbek translation!",
        "endpoints": {
            "/download": "Download a video from a URL.",
            "/convert": "Convert an audio file to mp3.",
            "/transcribe": "Transcribe an audio file to text.",
            "/translate": "Translate text to Uzbek.",
        },
    }


@app.post("/download")
async def download(
    video_input: VideoInput = VideoInput(
        url="https://youtu.be/foT9rsHmS24?si=was7pzbKrDNcUIVD"
    ),
):
    """
    Download the video file from the provided URL.
    """
    video_url = video_input.url

    if not video_url:
        return {"error": "No video URL provided."}

    # Download the video from the URL
    video_file = download_video(video_url)

    # Check if the video was downloaded successfully
    if (
        video_file is None
        or isinstance(video_file, str)
        and video_file.startswith("An error occurred")
    ):
        return {"error": "Failed to download the video."}

    return {"message": "Video downloaded successfully.", "video_file": video_file}


@app.post("/convert")
async def convert(
    audio_file: AudioInput = AudioInput(audio_file="temp_files/Lorem-Ipsum.wav"),
):
    """
    Convert the audio file to mp3.
    """
    audio_file = convert_to_mp3(audio_file.audio_file, "temp_files/audio.mp3")
    if isinstance(audio_file, str) and audio_file.startswith("An error occurred"):
        return {"error": audio_file}
    return {"message": "Audio converted successfully.", "audio_file": audio_file}


@app.post("/transcribe")
async def transcribe(
    audio_file: AudioInput = AudioInput(audio_file="temp_files/Lorem-Ipsum.wav"),
):
    """
    Transcribe the audio file to text.
    """
    transcription = transcribe_audio(audio_file.audio_file)
    if not transcription:
        return {"error": "Failed to transcribe audio."}
    return {"transcription": transcription}


@app.post("/translate")
async def translate(
    text: TextInput,
    source_lang: str = "en",
    target_lang: str = "uz",
):
    """
    Translate the text to Uzbek.
    """
    text = translate_text(text.text, source_lang=source_lang, target_lang=target_lang)
    if not text:
        return {"error": "Failed to translate text."}
    translated_text = f"Translated: {text}"
    return {"translated_text": translated_text}


@app.post("/translate-from-url")
async def translate_from_url(
    video_input: VideoInput = VideoInput(
        url="https://youtu.be/foT9rsHmS24?si=was7pzbKrDNcUIVD"
    ),
    source_lang: str = "en",
    target_lang: str = "uz",
):
    """
    Download the video file from the provided URL and translate it to Uzbek.
    """
    transcription = await collect_data(video_input.url, source_lang, target_lang)
    return {
        "message": "Video downloaded and translated successfully.",
        "video_file": video_input.url,
        "source_lang": source_lang,
        "target_lang": target_lang,
        "transcription": transcription,
    }


if __name__ == "__main__":
    # Run the FastAPI app with Uvicorn
    uvicorn.run("main:app", reload=True)
