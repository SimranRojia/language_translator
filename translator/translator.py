from googletrans import Translator, LANGUAGES

# Function to translate text
def translate_text(text, src_lang, dest_lang):
    try:
        translator = Translator()
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        return translation.text, LANGUAGES[dest_lang]
    except Exception as e:
        return f"Error: {str(e)}", None

# Function to convert language name to language code
def get_language_code(language_name):
    language_name = language_name.lower()
    for code, name in LANGUAGES.items():
        if name.lower() == language_name:
            return code
    return None
