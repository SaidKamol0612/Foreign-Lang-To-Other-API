import os
import uuid

from api.utils import (
    downloader,
    converter,
    separator,
    transcriber,
    translator,
)

FILES_DIR = "temp_files"


async def collect_data(
    url: str,
    from_lang: str = "en",
    to_lang: str = "uz",
) -> str:
    """
    Collect data from a given URL.

    Args:
        url (str): The URL to collect data from.

    Returns:
        str: The collected data.
    """
    created_files = []
    try:
        # Download the data from the URL
        audio_from_url = await downloader.download_video(
            url, output_path=f"{FILES_DIR}/{uuid.uuid4()}.webm"
        )
        created_files.append(audio_from_url)

        # Convert the audio to a suitable format
        audio_file = await converter.convert_to_mp3(
            audio_from_url, output_path=f"{FILES_DIR}/{uuid.uuid4()}.mp3"
        )
        created_files.append(audio_file)

        # Separate the audio into different chunks
        chunk_dir = f"{FILES_DIR}/chunks_{uuid.uuid4().hex}"
        audio_chunks = await separator.split_to_chunks(
            audio_file, output_dir=chunk_dir
        )
        created_files.extend(audio_chunks)

        # Transcribe the audio chunks to text
        full_transcript = ""
        for chunk in audio_chunks:
            transcript = await transcriber.transcribe_audio(chunk, from_lang)
            full_transcript += transcript + "\n"

        # Translate the transcript to Uzbek
        translated_transcript = await translator.translate_text(
            full_transcript, from_lang, to_lang
        )

        return translated_transcript
    finally:
        for file_path in created_files:
            if os.path.exists(file_path):
                os.remove(file_path)
                
        if 'chunk_dir' in locals() and os.path.exists(chunk_dir):
            os.rmdir(chunk_dir)
