from translate import Translator

# Function to translate text
def translate_text(text, target_language):
    translator = Translator(to_lang=target_language)
    translated = translator.translate(text)
    return translated

# Main program
if __name__ == "__main__":
    # Input the text you want to translate
    text_to_translate = input("Enter text in English: ")

    # Input the language to translate to (e.g., 'fr' for French, 'es' for Spanish)
    target_lang = input("Enter target language code (e.g., 'fr' for French, 'es' for Spanish): ")

    # Get the translation
    translated_text = translate_text(text_to_translate, target_lang)
    print(f"Translated text: {translated_text}")
