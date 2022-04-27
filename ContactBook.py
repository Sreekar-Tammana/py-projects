def showAllContacts():
    print('\n***ALL CONTACTS***\n')
    for i,(x,y) in enumerate(book.items()):
        print(f'({i+1}) . {x} : {y}')

def addContact():
    print('\n***ADD CONTACT***\n')
    name = input('Enter Name : ')
    phnum = int(input('Enter Phone Number : '))
    book[name] = phnum

def findContact():
    print('\n***FIND CONTACT***\n')
    try:
        findName = input('Enter the name of contact to search : ')
        print('Contact number : ',book[findName])
    except:
        print('No Match Found!\nEnsure that you entered name correctly...')

def updateContact():
    print('\n***UPDATE CONTACT***\n')
    updateName = input('Enter the contact name you want to update : ')
    updateNum = int(input('Enter the Phone number : '))
    book[updateName] = updateNum


if __name__=="__main__":

    book = {}

    run = True

    while run:

        print('\n(1). Show All Contacts\n(2). Add Contact\n(3). Find Contact\n(4). Update Contact\n(5). Quit\n')

        select = int(input('Enter choice : '))

        if select==1:
            showAllContacts()
        elif select==2:
            addContact()
        elif select==3:
            findContact()
        elif select==4:
            updateContact()
        elif select==5:
            run=False
