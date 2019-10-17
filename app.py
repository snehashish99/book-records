from util import database

USER_CHOICE = """
Enter:
a-add to list
l-list all books
r-mark as read
d-delete book
q-quit

Your choice: """

def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while(user_input != 'q'):
        if(user_input=='a'):
            prompt_add_book()

        elif(user_input == 'l'):
            list_books()

        elif(user_input == 'r'):
            prompt_read_book()

        elif(user_input == 'd'):
            prompt_delete_book()

        else:
            print("Unknown input")
        user_input = input(USER_CHOICE)
def prompt_add_book():
    name=input("Enter name of book: ")
    author=input("Enter author name: ")
    database.add_book(name, author)

def list_books():
    books=database.get_all_books()
    for book in books:
        print(book)

def prompt_read_book():
    name=input("Enter name of the book: ")
    database.mark_book_as_read(name)

def prompt_delete_book():
    name=input("Enter the name of book to be deleted: ")
    database.delete_book(name)


menu()