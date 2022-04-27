# Comparing element 1 in and element 2 in List and 
# return True if same or return False

list = []

n = int(input("Enter number of Elements : "))

for i in range(n):
    num = input(f"Enter element {i+1} : ")
    list.append(num)
    
if list[0]==list[len(list)-1]:
    print("\nTrue")
else:
    print("\nFalse")