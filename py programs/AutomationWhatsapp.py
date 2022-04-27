import pywhatkit

number = input("Number(including +91) : ")
msg = input("Enter message : ")
hour = int(input("Enter the hour : "))
min = int(input("Enter the minute : "))
amPm = input("Enter am or pm : ")

if amPm=="pm":
    hour += 12

pywhatkit.sendwhatmsg(number,msg,hour,min)