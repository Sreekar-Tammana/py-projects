# print the elements in list divisible by 5

list = []

n = int(input("Enter the Number of Elements : "))

for i in range(n):
    num = int(input(f"Enter the Element {i+1} : "))
    list.append(num)

for i in range(len(list)):
    if list[i]%5==0:
        print(f"\n{list[i]}")
    else:
        pass