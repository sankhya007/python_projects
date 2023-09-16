

# instsall the library using this function in cmd : pip install googletrans==4.0.0-rc1


from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

if __name__ == "__main__":
    print("Simple Language Translator")
    source_text = input("Enter the text to translate: ")
    target_language = input("Enter the target language (e.g., 'es' for Spanish, 'fr' for French): ")

    translated_text = translate_text(source_text, target_language)
    print(f"Translated text: {translated_text}")





# language_codes = {
#     "afrikaans": "af",
#     "albanian": "sq",
#     "amharic": "am",
#     "arabic": "ar",
#     "armenian": "hy",
#     "azerbaijani": "az",
#     "basque": "eu",
#     "belarusian": "be",
#     "bengali": "bn",
#     "bosnian": "bs",
#     "bulgarian": "bg",
#     "catalan": "ca",
#     "cebuano": "ceb",
#     "chichewa": "ny",
#     "chinese": "zh",
#     "corsican": "co",
#     "croatian": "hr",
#     "czech": "cs",
#     "danish": "da",
#     "dutch": "nl",
#     "english": "en",
#     "esperanto": "eo",
#     "estonian": "et",
#     "filipino": "tl",
#     "finnish": "fi",
#     "french": "fr",
#     "frisian": "fy",
#     "galician": "gl",
#     "georgian": "ka",
#     "german": "de",
#     "greek": "el",
#     "gujarati": "gu",
#     "haitian creole": "ht",
#     "hausa": "ha",
#     "hawaiian": "haw",
#     "hebrew": "iw",
#     "hindi": "hi",
#     "hmong": "hmn",
#     "hungarian": "hu",
#     "icelandic": "is",
#     "igbo": "ig",
#     "indonesian": "id",
#     "irish": "ga",
#     "italian": "it",
#     "japanese": "ja",
#     "javanese": "jw",
#     "kannada": "kn",
#     "kazakh": "kk",
#     "khmer": "km",
#     "kinyarwanda": "rw",
#     "korean": "ko",
#     "kurdish": "ku",
#     "kyrgyz": "ky",
#     "lao": "lo",
#     "latin": "la",
#     "latvian": "lv",
#     "lithuanian": "lt",
#     "luxembourgish": "lb",
#     "macedonian": "mk",
#     "malagasy": "mg",
#     "malay": "ms",
#     "malayalam": "ml",
#     "maltese": "mt",
#     "maori": "mi",
#     "marathi": "mr",
#     "mongolian": "mn",
#     "myanmar": "my",
#     "nepali": "ne",
#     "norwegian": "no",
#     "nyanja": "ny",
#     "odia": "or",
#     "pashto": "ps",
#     "persian": "fa",
#     "polish": "pl",
#     "portuguese": "pt",
#     "punjabi": "pa",
#     "romanian": "ro",
#     "russian": "ru",
#     "samoan": "sm",
#     "scots gaelic": "gd",
#     "serbian": "sr",
#     "sesotho": "st",
#     "shona": "sn",
#     "sindhi": "sd",
#     "sinhala": "si",
#     "slovak": "sk",
#     "slovenian": "sl",
#     "somali": "so",
#     "spanish": "es",
#     "sundanese": "su",
#     "swahili": "sw",
#     "swedish": "sv",
#     "tajik": "tg",
#     "tamil": "ta",
#     "telugu": "te",
#     "thai": "th",
#     "turkish": "tr",
#     "ukrainian": "uk",
#     "urdu": "ur",
#     "uyghur": "ug",
#     "uzbek": "uz",
#     "vietnamese": "vi",
#     "welsh": "cy",
#     "xhosa": "xh",
#     "yiddish": "yi",
#     "yoruba": "yo",
#     "zulu": "zu"
# }
