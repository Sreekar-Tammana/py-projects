import requests

# 1. Write a Python code to find the Requests module – version, licence, 
# copyright information, author, author email, document url, title and description

# print('Version of Requests Module : ',requests.__version__)
# print('Licence : ',requests.__license__)
# print('Copyright Information : ',requests.__copyright__)
# print('Author : ',requests.__author__)
# print('Author Email : ',requests.__author_email__)
# print('URL : ',requests.__url__)
# print('Title : ',requests.__title__)
# print('Description : ',requests.__description__)

# ***********************************************************************************************

# 2. Write a Python code to check the status code issued by a server in response to a client's request
#  made to the server. Print all of the methods and attributes available to objects on successful request

# res = requests.get('https://meet.google.com/')
# print(f'Google Meet Status Code : {res.status_code}')

# res1 = requests.get('https://www.youtube.com/')
# print(f'Youtube Status Code : {res1.status_code}')

# res2 = requests.get('https://www.geeksforgeeks.org/c-plus-plus/')
# print(f'GeeksforGeeks Dir : {dir(res2)}')

# ***************************************************************************************************

# 3. Write a Python code to send a request to a web page, and print the response text and content

# res = requests.get('https://www.youtube.com/')
# print('Youtube Text : ',res.text)
# print('*****************************************************************************')
# res1 = requests.get('https://meet.google.com/')
# print('Google Meet Content : ',res1.content)

# ********************************************************************************************************

# 4. Write a Python code to send a request to a web page, and print the information of headers.
#  Also parse these values and print key-value pairs holding various information

# r = requests.get('https://www.youtube.com/')
# res = r.headers
# print(f'Headers of Youtube :\n',res)

# for item in res:
#     print(f'{item} : {res[item]}\n')

# ********************************************************************************************************

# 5. Write a Python code to send a request to a web page, and print the JSON value of the response.
#  Also print each key value of the response

# r = requests.get('https://api.github.com/')

# req = r.json()
# print(r.json())

# for item in req:
#     print(f'{item} : {req[item]}\n')

# *************************************************************************************************************

