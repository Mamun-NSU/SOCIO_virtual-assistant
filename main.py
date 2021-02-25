import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
socio = pyttsx3.init()
voices = socio.getProperty('voices')
socio.setProperty('voices', voices[1].id)
socio.say('How can i help you')
socio.runAndWait()

try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)

except:
    pass
