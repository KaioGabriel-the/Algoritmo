import os
import speech_recognition as sr

def ouvirMicrofone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)

        print("Diga algo: ")

        audio = microfone.listen(source)

    try:
        
        frase = microfone.recognize_google(audio,language="pt-br")

        print("Você disse: "+ frase)
        return False

    except sr.UnknownValueError:
        print("Não entendi")
        return True
    
while True: 
    if not ouvirMicrofone():
        break
