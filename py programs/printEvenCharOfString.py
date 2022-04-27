# print even index number of string

str = "pynative"

for i in range(len(str)):
    if i%2==0:
        print(str[i])
    else:
        pass

# Short and Easy Method 

str = "pynative"

for i in range(0 , len(str) , 2):
    print(str[i])