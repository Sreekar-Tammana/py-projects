# map and reduce , filter

#1. Write a Python program to triple all numbers of a given list of integers. Use Python map

# nums = [1,4,5,3,8,9,2]

# tripleNum = list(map(lambda x: x*3,nums))
# print(tripleNum)

# ****************************************************************************************

#2. Write a Python program to add three given lists using Python map and lambda

# l1 = [4,7,9]
# l2 = [6,2,0]
# l3 = [2,4,8]

# result = list(map(lambda x,y,z: x+y+z ,l1,l2,l3))
# print(result)

# ******************************************************************************************

#3.  Write a Python program to listify the list of given strings individually using Python map

# strings =  ["This is an Indiviual string"]

# indi = list(map(list,strings))
# print(indi)

# ********************************************************************************************

#4. Write a Python program to square the elements of a list using map() function

# lst = [1,2,3,4,5,6,7,8,9]

# square_ele = map(lambda x: x**x,lst)
# print(list(square_ele))

# **************************************************************************************************

#5.  Write a Python program to add two given lists and
#  find the difference between lists. Use map() function

# lst1 = [3,6,5,1,6,8]
# lst2 = [9,1,2,0,2,7]

# add_sub = map(lambda x,y: (x+y,x-y),lst1,lst2)
# print(list(add_sub))

# ***************************************************************************************************

#6.  Write a Python program to convert 
# a given list of integers and a tuple of integers in a list of strings

# lst_nums = [5,3,8,2]
# tuple_nums = (3,1,9,4)

# convert_lst = list(map(str,lst_nums))
# convert_tuple = tuple(map(str,tuple_nums))
# print(convert_lst)
# print(convert_tuple)

# *****************************************************************************************************

#7. Write a Python program to create a new list taking specific elements 
# from a tuple and convert a string value to integer.

data = [('Rehitho','12/3/1999','38kg'),('xavier','12/12/1912','65kg'),('macha','23/1/1997','2kg')]

# print('Orginal list : ',data)
# student_names = list(map(lambda name:name[0],data))
# print('Student Names : \n')
# print(student_names)
# student_dates = list(map(lambda date: date[1],data))
# print('Students Dates : \n')
# print(student_dates)
# student_weight = list(map(lambda weight: int(weight[2][:-2]),data))
# print('Students Weight : \n')
# print(student_weight)

# **************************************************************************************************

# 8. Write a Python program to count the same pair in two given lists. use map() function

# nums1 = [2,5,4,1,6,8,6,1,2]
# nums2 = [2,3,4,5,6,7,8,1,3]

# common_ele = list(map(lambda x,y: x==y,nums1,nums2))
# print(common_ele)