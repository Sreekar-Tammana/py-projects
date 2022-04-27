import datetime
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
print(voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)

def take_command():
    r = sr.Recognizer() # helps to recoginze the voice
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f'user said : {query}')

    except Exception as e:
        print('Sorry , Can you Please say that again')
        return "none"

Htime = datetime.datetime.now().hour
Mtime = datetime.datetime.now().minute
# print(Htime,Mtime)
speak(f"{Htime} : {Mtime}")

