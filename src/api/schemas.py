from pydantic import BaseModel


class VideoInput(BaseModel):
    url: str


class AudioInput(BaseModel):
    audio_file: str


class TextInput(BaseModel):
    text: str
