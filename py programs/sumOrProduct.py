# Question : if product of two numbers is greater than 1000 then return their sum

# With use of FUNCTION

def sumorproduct(a,b):
    if a*b>1000:
        return a+b
    else:
        return a*b

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

print(sumorproduct(num1,num2))

# Normal Method 

x = int(input("Enter num x : "))
y = int(input("Enter num y : "))

if x*y>1000:
    print(x+y)
else:
    print(x*y)