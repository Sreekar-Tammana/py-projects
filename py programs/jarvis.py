import datetime
import pyttsx3
import pyaudio
import speech_recognition as sr
import os
import webbrowser

engine = pyttsx3.init()  # intializing the speech engine
voices = engine.getProperty('voices')  # getting the voices which are inBuilt
engine.setProperty('voice', voices[2].id)  # setting the voice we required
rate = engine.getProperty('rate')  # rate is to control the speed of voice
engine.setProperty('rate', 150)  # setting the rate of voice

# This Function Always Executes 1st
def wishMe():
    # taking the Hour time into a variable
    HrTime = int(datetime.datetime.now().hour)

    # taking the Minute time into variable
    MinTime = int(datetime.datetime.now().minute)

    if HrTime < 12:  # executes when time is (1AM to 11:59AM)
        speak(
            f'Good Morning Sreekar , the time is {HrTime} {MinTime}AM , Im Zeera...How may I Help You')
    elif HrTime > 12 and HrTime-12 < 6: # executes when time is (12PM to 5:59PM)
        speak(
            f'Good Afternoon Sreekar , the time is {HrTime-12} {MinTime}PM , Im Zeera...How may I Help You')
    elif HrTime-12 >= 6 and HrTime-12 < 10: # executes when time is (6PM to 9:59PM)
        speak(
            f'Hello! Sreekar, its Evening , the time is {HrTime-12}:{MinTime}PM , Im Zeera...How may I Help You')
    elif HrTime-12 >= 10 and HrTime-12 < 12: # executes when time is (10PM to 11:59PM)
        speak(f'Ohhh Sreekar Its {HrTime-12} {MinTime}PM , Its time to Sleep')

# This Function Converts the Text to Speech
def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

# This Function takes voice command from user
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

    return query


if __name__ == "__main__":
    wishMe()
    # speak('Sreekar I Love UUUU soooooooo much , Please Accept My Love Otherwise i will kill your Bestfriend Saathvika')
    query = take_command().lower() # converts the voice into the lower letters
    quit = False
    while True:
        # if 'open youtube' in query:
        #     webbrowser.open("youtube.com")  # SOMETHING WRONG WITH THIS CODE
        # WHEN IT IS EXECUTED IT IS OPENING MULTIPLE TABS
        # webbrowser.open