import os

from pydub import AudioSegment

async def split_to_chunks(
    audio_file: str, chunk_length_ms: int = 30000, output_dir: str = "temp_files/chunks"
) -> list:
    """
    Split an audio file into chunks of specified length.

    Args:
        audio_file (str): Path to the audio file.
        chunk_length_ms (int): Length of each chunk in milliseconds.
        output_dir (str): Directory to save the chunks.

    Returns:
        list: List of paths to the saved chunks.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    audio = AudioSegment.from_file(audio_file)
    chunks = []

    if (len(audio) // 1000) < 300:
        chunks.append(audio_file)
        return chunks
    
    for i, start in enumerate(range(0, len(audio), chunk_length_ms)):
        chunk = audio[start:start + chunk_length_ms]
        chunk_path = os.path.join(output_dir, f"chunk_{i}.wav")
        chunk.export(chunk_path, format="wav")
        chunks.append(chunk_path)

    return chunks