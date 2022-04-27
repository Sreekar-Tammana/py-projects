# take odd number from list1 and even number from list2 and merge in new_list

def OddAndEven(x=[] ,y=[],z=[]):
    for i in range(len(x)):
        if x[i]%2==1:
            z.append(x[i])

    for i in range(len(y)):
        if y[i]%2==0:
             z.append(y[i])

# Here Lists are Declared in Program

# list1 = [1 , 2 , 3, 4, 5]
# list2 = [1 , 2 ,3 , 4, 5]

# newList = []

# OddAndEven(list1,list2,newList)

# print(newList)

# Solving Using Function and User Input

l1 = []
l2 = []
nl = []

num1 = int(input("Enter the Size of List 1 : "))

for i in range(num1):
    data1 = int(input(f"Enter Element {i+1} : "))
    l1.append(data1)

num2 = int(input("Enter the Size of List 2 : "))

for j in range(num2):
    data2 = int(input(f"Enter Element {j+1} : "))
    l2.append(data2)

OddAndEven(l1,l2,nl)

print("The new List is : ",nl)















