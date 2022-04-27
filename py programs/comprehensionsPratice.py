#1. Find all of the numbers from 1-1000 that are divisible by 7

# numDivBySeven = [number for number in range(1000) if number%7==0]
# print(numDivBySeven)

# ***************************************************************************************************

#2. Find all of the numbers from 1-1000 that have a 3 in them

# havingThree = [num for num in range(1000) if '3' in str(num)]
# print(havingThree)

# ******************************************************************************************************

#3. Count the number of spaces in a string

# sentence = "This is me as you as said everyone is not me as u and me as there in 2020"
# countSpaces = [character for character in sentence if character==' ']
# countSpaces = sentence.count(" ") #this is another method
# print(len(countSpaces))

# *****************************************************************************************************

#4. Remove all of the vowels in a string

# sentence = "This is me as you as said everyone is not me as u and me as there in 2020"
# vowels = ['a','e','i','o','u']
# removeVowels = [letter for letter in sentence if letter.lower() not in vowels]
# print(removeVowels)

# *******************************************************************************************************

#5. Find all of the words in a string that are less than 4 letters

# sentence = "This is me as you as said everyone is not me as u and me as there in 2020"

# words = list(sentence.split())

# lessThanFourLetters = [words for words in words if len(words)<4]
# print(lessThanFourLetters)

# *******************************************************************************************************

#6. Use a dictionary comprehension to count the length of each word in a sentence

# sentence = "This is me as you as said everyone is not me as u and me as there in 2020"

# words = list(sentence.split())

# myDict = {word : len(word) for word in words}
# print(myDict)

# *******************************************************************************************************