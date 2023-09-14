# less fast but more accurate.


import speech_recognition as sr

def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening... Say something:")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise

        try:
            audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds
            print("Recognizing...")

            # Use the Google Web Speech API for recognition
            text = recognizer.recognize_google(audio)
            return text

        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected.")
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Error connecting to the Google API: {e}")

if __name__ == "__main__":
    result = speech_to_text()
    if result:
        print(f"Text: {result}")








#faster but more error 



# import speech_recognition as sr

# def speech_to_text():
#     # Initialize the recognizer
#     recognizer = sr.Recognizer()

#     # Use the default microphone as the audio source
#     with sr.Microphone() as source:
#         print("Listening... Say something:")
#         recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise

#         try:
#             audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds
#             print("Recognizing...")

#             # Use the PocketSphinx recognizer for recognition
#             text = recognizer.recognize_sphinx(audio)
#             return text

#         except sr.WaitTimeoutError:
#             print("Listening timed out. No speech detected.")
#         except sr.UnknownValueError:
#             print("Could not understand audio.")

# if __name__ == "__main__":
#     result = speech_to_text()
#     if result:
#         print(f"Text: {result}")








# HAHA bullshit 

# import speech_recognition as sr
# from langdetect import detect

# def speech_to_text_and_language():
#     # Initialize the recognizer
#     recognizer = sr.Recognizer()

#     # Use the default microphone as the audio source
#     with sr.Microphone() as source:
#         print("Listening... Say something:")
#         recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise

#         try:
#             audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds
#             print("Recognizing...")

#             # Use the PocketSphinx recognizer for speech recognition
#             text = recognizer.recognize_sphinx(audio)
#             print(f"Recognized Text: {text}")

#             # Use langdetect for language detection
#             language = detect(text)
#             print(f"Detected Language: {language}")

#             return text, language

#         except sr.WaitTimeoutError:
#             print("Listening timed out. No speech detected.")
#         except sr.UnknownValueError:
#             print("Could not understand audio.")

# if __name__ == "__main__":
#     result_text, result_language = speech_to_text_and_language()
#     if result_text:
#         print(f"Text: {result_text}")
#     if result_language:
#         print(f"Language: {result_language}")



