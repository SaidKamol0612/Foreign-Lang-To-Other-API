import os
from faster_whisper import WhisperModel

model = WhisperModel("small", compute_type="int8", device="cpu")

async def transcribe_audio(file_path: str, source_lang: str = "en") -> str:
    """
    Transcribe audio file to text using Whisper model.

    Args:
        file_path (str): Path to the audio file.

    Returns:
        str: Transcribed text or error message.
    """
        
    if not os.path.exists(file_path):
        return f"Error: The file '{file_path}' does not exist."

    try:
        segments, _ = model.transcribe(file_path, language=source_lang, beam_size=5)
        transcription = " ".join([segment.text for segment in segments])
        return transcription
    except Exception as e:
        return f"An error occurred during transcription: {e}"
