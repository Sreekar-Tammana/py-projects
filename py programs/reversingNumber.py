# Reversing number 
# Generally this Method is used to Reverse String
# Reversing number have another method to Reverse 

num = input("Enter the number to reverse : ")

rev_num = num[::-1]

if rev_num==num:
    print("\nOriginal Number is Same as Reversed Number")
else:
    print("\nOriginal Number is Not same as Reversed Number")