import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
def main():
  
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("Recognizing...")
        audio_data = r.listen(source)
        # convert speech to text
        text = r.recognize_google(audio_data, language='ru-RU')
        print(text)
        return text