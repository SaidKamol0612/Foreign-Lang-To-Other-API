from googletrans import Translator


async def translate_text(text: str, source_lang: str = "en", target_lang: str = "uz") -> str:
    """
    Translate the given text from English to Uzbek using Google Translate API.
    """
    translator = Translator()
    try:
        translated = translator.translate(text, src=source_lang, dest=target_lang)
        return translated.text
    except Exception as e:
        return f"An error occurred during translation: {str(e)}"
