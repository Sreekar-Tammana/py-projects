# METHOD 1

# email = []

# mail = input('Enter your mail Id : ')

# for i in range(len(mail)):
#     if mail[i]=='@':
#         break
#     email.append(mail[i])

# print('UserName :',''.join(email[i] for i in range(len(email))))

# for i in range(len(mail)):
#     if mail[i]=='@':
#         print('Domain :',mail[i+1:])

# METHOD 2

email = input('Enter you Id : ').strip()

try:
    UserName = email[:email.index('@')]

    Domain = email[email.index('@')+1:]

    print(f'UserName : {UserName}\nDomain : {Domain}')
except:
    print('Please enter a valid Id:(')