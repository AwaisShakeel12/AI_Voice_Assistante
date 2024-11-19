
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
      

# voice_input()


def text_to_speech(text):
    tts=gTTS(text=text, lang="en")
    
    #save the speech from the given text in the mp3 format
    tts.save("speech.mp3")

def llm_model_object(user_text):
    #model = "models/gemini-pro"
    
    genai.configure(api_key='AIzaSyDFRjqJh9PUrBXclbyICiNGfaKZ3Om6Lu0')
    
    model = genai.GenerativeModel('gemini-1.5-flash', )
    
    response=model.generate_content(user_text, 
        generation_config=genai.types.GenerationConfig(
        candidate_count=1,
        # stop_sequences=['x'],
        max_output_tokens=50,
        temperature=0.2
       )
    )
    print(f"Response from LLM: {response}")
    result=response.text
    
    return result
