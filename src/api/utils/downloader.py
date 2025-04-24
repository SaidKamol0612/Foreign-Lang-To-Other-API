import yt_dlp


async def download_video(url: str, output_path: str) -> str:
    """
    Downloads a YouTube video and saves the audio without using ffmpeg.

    Args:
        url (str): The URL of the YouTube video to download.
        output_path (str): The path where the downloaded audio file will be saved.

    Returns:
        str: The file path of the downloaded audio or an error message.
    """
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": output_path,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return output_path
    except Exception as e:
        return f"An error occurred: {e}"
