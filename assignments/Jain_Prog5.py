# Name : Vinit Kirit Jain
# Creation Date : 2023-11-13
""" Brief Description :
    This program is a basic book management system in Python. 
    It enables users to add, delete, and view individual records, as well as display all book records stored in a text file through a simple menu.
"""

# importing the os module for file operations
import os

# prompting the user for input
user_name = input("please enter your username: ")
# printing a greeting message with the entered username
print("hello, " + user_name + "!!!")


# defining a book class with attributes: title, author, publication_date, price, readers
class Book:
    def __init__(self, title, author, publication_date, price, readers):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.price = price
        self.readers = readers


# defining a function to read all records from the file
def read_all_records():
    print("all the contents of the file:\n")
    print("title\tauthor\tpublication date\tprice\treaders")
    with open("./BookShop.txt", "r") as file_object:
        for i in file_object.readlines():
            # creating a book object from the comma-separated values
            book_object = Book(*i.split(","))
            print(
                book_object.title
                + "\t"
                + book_object.author
                + "\t"
                + book_object.publication_date
                + "\t"
                + book_object.price
                + "\t"
                + book_object.readers
            )


# defining a function to read a specific record based on the author's name
def read_record(author_search):
    print("search results: \n")
    print("title\tauthor\tpublication date\tprice\treaders")
    with open("./BookShop.txt", "r") as file_object:
        for i in file_object.readlines():
            # creating a book object from the comma-separated values
            book_object = Book(*i.split(","))
            if author_search == book_object.author:
                print(
                    book_object.title
                    + "\t"
                    + book_object.author
                    + "\t"
                    + book_object.publication_date
                    + "\t"
                    + book_object.price
                    + "\t"
                    + book_object.readers
                )
    input("press a key to continue: ")


# defining a function to display the menu options
def show_menu():
    print(
        "please select one option and press enter\n1. add a book\n2. delete a book\n3. view a book\n4. view the book file\n5. exit"
    )
    selected_option = int(input("please select one option and press enter: "))
    return selected_option


# defining a function to add a book to the file
def add_book_to_file(filename, book):
    with open(filename, "a+") as file_object:
        file_object.write(
            ",".join(
                [
                    book.title,
                    book.author,
                    book.publication_date,
                    book.price,
                    book.readers,
                ]
            )
            + "\n"
        )


# defining a function to delete a book from the file
def delete_book_from_file(filename, author_name):
    with open(filename, "r") as file_object:
        for i in file_object.readlines():
            # creating a book object from the comma-separated values
            book_object = Book(*i.split(","))
            with open("./BookShop-Temp.txt", "a+") as new_file_object:
                if author_name != book_object.author:
                    new_file_object.write(
                        ",".join(
                            [
                                book_object.title,
                                book_object.author,
                                book_object.publication_date,
                                book_object.price,
                                book_object.readers,
                            ]
                        )
                    )
    os.remove(filename)  # removing the original file
    # renaming the temporary file to the original name
    os.rename("BookShop-Temp.txt", "BookShop.txt")


# defining the main function
def main():
    # initializing the input_option variable
    input_option = 0
    # continuing the loop until the user chooses option 5 (exit)
    while input_option != 5:
        # option to add a book
        if input_option == 1:
            # initializing an empty dictionary for book details
            book_dictionary = {}
            for i in ["title", "author", "publication date", "price", "readers"]:
                book_dictionary[i]
