import ffmpeg
import os


async def convert_to_mp3(input_path: str, output_path: str) -> str:
    """
    Converts a video file to MP3 format using ffmpeg.

    Args:
        input_path (str): The path of the input video file.
        output_path (str): The path where the converted MP3 file will be saved.

    Returns:
        str: The file path of the converted MP3 file or an error message.
    """
    if not os.path.exists(input_path):
        return f"Input file not found: {input_path}"

    try:
        ffmpeg.input(input_path).output(output_path, format="wav").run(
            quiet=False, capture_stdout=True, capture_stderr=True
        )
        return output_path
    except ffmpeg.Error as e:
        return f"FFmpeg error: {e.stderr.decode()}"
    except Exception as e:
        return f"An error occurred: {e}"
