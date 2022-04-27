#1. Write a Python program to read an entire text file

# with open('poem.txt','r') as f:
#     print(f.read())

# *******************************************************************************

#2. Write a Python program to read first n lines of a file

# n = int(input("Enter number of lines you want to read : "))
# with open('poem.txt') as f:
#     for line in range(n):
#         print(f.readline(),end='')

# *********************************************************************************

#3.  Write a Python program to append text to a file and display the text

# with open('poem.txt','a') as f:
#     text = input("Enter the line : ")
#     f.write("\n"+text)

# with open('poem.txt') as f:
#     print(f.read(),end=' ')

# *********************************************************************************

#4.  Write a Python program to read a file line by line and store it into a list

# with open('poem.txt') as f:
#     print(f.readlines())

# **********************************************************************************

#5. Write a Python program to read a file line by line store it into a variable

# with open('poem.txt') as f:
#     lst = f.readlines()
#     print(lst)

# **********************************************************************************

#6.  Write a Python program to read a file line by line store it into an array

# arr = []
# with open('poem.txt') as file:
#     for line in file:
#         arr.append(line)
# print(arr)

# **********************************************************************************

#7. Write a python program to find the longest word

# with open('poem.txt') as file:
#     lst = file.readlines()
#     max_len = len(max(lst,key=len))

# for line in lst:
#     if len(line)==max_len:
#         print(line)

# **************************************************************************************

#8. Write a Python program to count the number of lines in a text file

# with open('poem.txt') as f:
#     text = f.readlines()
#     print(len(text))

# **************************************************************************************

#9. Write a Python program to count the frequency of words in a file

# with open('poem.txt') as f:
#     words = f.read().split()
#     print(words)
#     print(len(words))

# ****************************************************************************************

#10. Write a Python program to write a list to a file

# animals = ['dog','cat','elephant','zebra','tortoise']

# with open('animals.txt','w+') as f:
#     for i in animals:
#         f.write(i+"\n")

# text = open('animals.txt')
# print(text.read())

# ******************************************************************************************