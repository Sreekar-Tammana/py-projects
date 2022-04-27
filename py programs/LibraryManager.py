class Library:

    def __init__(self,books_list,library_name):
        self.lend_data = {}
        self.books_list = books_list
        self.library_name = library_name

        for books in self.books_list:
            self.lend_data[books] = None

    def show_books(self): #For Displaying Boooks
        for index,book in enumerate(self.books_list):
            print(f"{index+1} : {book}")
            
    def add_book(self,book_name): #To add a book to list
        self.books_list.append(book_name)
        self.lend_data[book_name] = None

    def lend_book(self,reader,book_lend):
        if book_lend in self.books_list:
            if self.lend_data[book_lend] is None:
                self.lend_data[book_lend] = reader
                print('Book Lended')
            else:
                print(f'Already this book is Lended by {self.lend_data[book_lend]}')
        else:
            print('Please check the book name you entered')

    def return_book(self,user,book_name):
        if book_name in self.books_list:
            if self.lend_data[book_name] is not None:
                self.lend_data.pop(book_name)
                print('Book Returned successfully')
            else:
                print('Sorry the book is not lend...')
        else:
            print('Check the book name correctly')

    def delete_book(self,book):
        self.books_list.remove(book)
        self.lend_data.pop(book)

if __name__ == "__main__":

    library_name = 'sreekar'
    books_list = ['Sherlock Homles','Rich Dad and Poor Dad','Harry Potter','Moon Walk With Einstein']
    sreekar = Library(books_list,library_name)
    security_key = 1234
    print('\n\t\t***LIBRARY MANAGER***\n')

    exit = False

    while exit!=True:
        print('\n\tOPTIONS : \n')
        print('\n\t(1). Show Books\n\t(2). Add Book\n\t(3). Lend Book\n\t(4). Return Book\n\t(5). Delete Book\n\t(6). Quit\n')
        option = input('Select an Option : \n')

        if option=='1':
            sreekar.show_books()
    
        if option=='2':
            input1 = input('Enter Book name : ')
            sreekar.add_book(input1)

        if option=='3':
            name_input = input('Enter Your Name : ')
            book_input = input('Enter the Book name : ')
            sreekar.lend_book(name_input,book_input)

        if option=='4':
            user = input('Enter your name : ')
            book_name = input('Enter book want to return : ')
            sreekar.return_book(user,book_name)

        if option=='5':
            password = int(input('Enter the key : '))
            if password==security_key:
                book_name = input('Enter the book name want to delete : ')
                sreekar.delete_book(book_name)
            else:
                print('Password Wrong...Unable to delete the book !')
        
        if option=='6':
            exit=True