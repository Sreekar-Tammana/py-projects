#1. Write a Python program to convert an integer to a roman numeral

# class Converter:

#     def int_to_roman(self,x):

#         nums = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
#         romans = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']

#         i =12
#         roman_ans = ''

#         while x !=0:
#             if nums[i]<=x:
#                 roman_ans+=romans[i]
#                 x-=nums[i]
#             else:
#                 i-=1
#         return roman_ans

# print(Converter().int_to_roman(1249))

# *****************************************************************************

#2. Write a Python program to convert an romal number to a integer

# class Converter:

#     def roman_to_int(self,string):
        
#         int_ans = 0
#         dict_roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

#         for i in range(len(string)):
#             if i > 0 and string[i] > string[i-1]:
#                 int_ans += dict_roman[string[i]] - 2*dict_roman[string[i-1]]
#             else:
#                 int_ans += dict_roman[string[i]]
#         return int_ans

# print(Converter().roman_to_int('XI'))