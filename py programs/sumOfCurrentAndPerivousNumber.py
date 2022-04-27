# print Current and perivous numbers and show sum of both of them

i = int(input("Enter the number of iterations : "))

for i in range(i+1):
    if i==0:
        print(f"Current Num : {i} , Pervious Num : {i} , Sum of both : {i}")
    else:
        print(f"Current Num : {i} , Pervious Num : {i-1} , Sum of both : {(i-1)+i}")