import random

list = ["snake", "water", "gun"]

print("\n\n********SNAKE WATER GUN********")

# comp = random.choice(list) # in this computer chooses the random word from the list

# user = input("Enter your choice from {list} : ")

# user = user.lower()

while True:
    comp = random.choice(list)
    user = input("\nEnter your choice Snake or Water or Gun :\n")
    user = user.lower()

    if user=="snake":
        if comp=="water":
            print("User WINS...:) :)\n")
        elif comp=="gun":
            print("Computer WINS...:)\n")
        else:
            print("Match DRAW...:(\n")

    elif user=="water":
        if comp=="snake":
            print("Computer WINS...:)\n")
        elif comp=="gun":
            print("User WINS...:) :)\n")
        else:
            print("Match DRAW...:(\n")
    
    elif user=="gun":
        if comp=="snake":
            print("User WINS...:) :)\n")
        elif comp=="water":
            print("Computer WINS...:)\n")
        else:
            print("Match DRAW...:(\n")
    
    else:
        pass