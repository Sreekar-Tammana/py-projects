import datetime
from pygame import mixer
from playsound import  playsound

def playAlarm (file, stop):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(True)
    user = input("Hit \"enter\" to stop alarm : ")
    if user == stop:
        mixer.music.stop()


print("\n****Values to set Alarm****")
aHour = int(input("Enter the Hour : "))
aMin = int(input("Enter the Minute : "))
amOrPm = input("Enter am or pm : ")

if amOrPm == "pm":
    aHour += 12

while True:
    if ( aHour == datetime.datetime.now().hour and aMin == datetime.datetime.now().minute ):
        print(f"Time to wake up buddy {datetime.datetime.now()}: ")
        playAlarm('charlie.mp3', ' ')
        break
