# Addition

add = lambda a,b : a+b
# print("Addition is : "+str(add(2,5)))

# *******************************************************************************

#1. Write a Python program to sort a list of tuples using Lambda

lst_tuple = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

lst_tuple.sort(key=lambda x: x[1]) #sorts based on marks
lst_tuple.sort(key=lambda x: x) #sorts based on subjects
# print(lst)

# *************************************************************************************

#2. Write a Python program to sort a list of dictionaries using Lambda

lst_dic = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

lst_dic.sort(key=lambda x: x['color'])
# print(lst_dic)

# ************************************************************************************

#3. Write a Python program to filter a list of integers using Lambda

numbers = [1,2,3,4,5,6,7,8,9]

even = list(filter(lambda x: x%2==0, numbers))
odd = list(filter(lambda x: x%2!=0, numbers))
# print(even)
# print(odd)

# ***************************************************************************************

#4.  Write a Python program to square and cube every number in a given list of integers using Lambda

nums = [1,2,3,4,5,6,7,8,9]

square_nums = list(map(lambda x: x**2,nums))
cubic_nums = list(map(lambda x: x**3,nums))

# print(square_nums)
# print(cubic_nums)

# **********************************************************************************************

#5.  Write a Python program to check whether a given string is number or not using Lambda

# string = input("Ënter any string : ")

# numOrNot = lambda x: x[1:].isnumeric() if x[0]=='-' else x.isnumeric()
# result = numOrNot(string)
# print(result)

# ******************************************************************************************