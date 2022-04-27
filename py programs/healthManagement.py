# Developed by Sreekar
# HEALTH MANAGEMENT

import datetime


def gettime():
    return datetime.datetime.now()

def addElements():
        yoyo = input("Enter Element : ")
        list.append(yoyo)
        return list

print("\n\n********HEALTH MANAGEMENT********")
print("Choose a client using numbers : ")
list = ["1.Harry", "2.Emma", "3.Roshan"]
with open("list.txt","a") as f:
    for item in list:
        print(item)

ik = input("Want To Add Element ? : ")
if ik=='s':
    addElements()

else:
    pass

for item in list:
    print(item)

n = int(input("Enter number of Client : "))

if n == 1:  # Client1 entering Data
    print("***Want to***\n1.Enter Data\n2.Retrive Data\n")
    w = int(input("Choose a Option : "))
    if w == 1:
        print("Enter Data of :\n1.Excersize\n2.Food")
        x = int(input("Select a option : "))
        if x == 1:
            val = input("Enter Excersize You Have Done : ")
            with open('HarryEx.txt', 'a') as f:
            #  with open('{list[0]}Ex.txt', 'a') as f:
                f.write(str([str(gettime())])+": "+val+"\n")
            print("Written Successfully")
        else:
            val1 = input("Enter Food You Have Ate : ")
            with open("HarryFood.txt", "a") as f:
                f.write(str([str(gettime())])+": "+val1+"\n")
            print("Written Successully")

    if w == 2:
        print("Retrive Data of :\n1.Excersize\n2.Food")
        x = int(input("Select a option : "))
        if x == 1:
            with open("HarryEx.txt") as f:
                for i in f:
                    print(i, end="")
        else:
            with open("HarryFood.txt") as f:
                for i in f:
                    print(i, end="")


if n == 2:
    print("***Want to***\n1.Enter Data\n2.Retrive Data\n")
    w = int(input("Choose a Option : "))
    if w == 1:
        print("Enter Data of :\n1.Excersize\n2.Food")
        x = int(input("Select a option : "))
        if x == 1:
            val = input("Enter Excersize You Have Done : ")
            with open('EmmaEx.txt', 'a') as f:
                f.write(str([str(gettime())])+": "+val+"\n")
            print("Written Successfully")
        else:
            val1 = input("Enter Food You Have Ate : ")
            with open("EmmaFood.txt", "a") as f:
                f.write(str([str(gettime())])+": "+val1+"\n")
            print("Written Successully")

    if w == 2:
        print("Retrive Data of :\n1.Excersize\n2.Food")
        x = int(input("Select a option : "))
        if x == 1:
            with open("EmmaEx.txt") as f:
                for i in f:
                    print(i, end="")
        else:
            with open("EmmaFood.txt") as f:
                for i in f:
                    print(i, end="")


if n == 3:
    print("***Want to***\n1.Enter Data\n2.Retrive Data\n")
    w = int(input("Choose a Option : "))
    if w == 1:
        print("Enter Data of :\n1.Excersize\n2.Food")
        x = int(input("Select a option : "))
        if x == 1:
            val = input("Enter Excersize You Have Done : ")
            with open('RoshanEx.txt', 'a') as f:
                f.write(str([str(gettime())])+": "+val+"\n")
            print("Written Successfully")
        else:
            val1 = input("Enter Food You Have Ate : ")
            with open("RoshanFood.txt", "a") as f:
                f.write(str([str(gettime())])+": "+val1+"\n")
            print("Written Successully")

    if w == 2:
        print("Retrive Data of :\n1.Excersize\n2.Food")
        x = int(input("Select a option : "))
        if x == 1:
            with open("RoshanEx.txt") as f:
                for i in f:
                    print(i, end="")
        else:
            with open("RoshanFood.txt") as f:
                for i in f:
                    print(i, end="")

