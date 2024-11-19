
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

import speech_recognition as sr

def voice_input():
    r = sr.Recognizer()
    with sr.Microphone(device_index=3) as source:
        print("listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("you said: ", text)
        return text
    except sr.UnknownValueError:
        print("sorry, could not understand the audio")
    except sr.RequestError as e:
        print("could not request result from google speech recognition service: {0}".format(e))



listn_test = voice_input()      
print(listn_test)


