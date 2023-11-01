user_name = input("Please enter your username: ")
print("Hello, " + user_name + "!!!")


class Book:
    def __init__(self, title, author, publication_date, price, readers):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.price = price
        self.readers = readers


def show_menu():
    print(
        "1. Add a book\n2. Delete a book\n3. View a book\n4. View the book file\n5. Exit"
    )
    selected_option = int(input("Please select one option and press enter: "))
    return selected_option


def add_book_to_file(filename, book):
    file_object = open(filename, "a")
    file_object.write(",".join(book))
    file_object.close()


def main():
    input_option = show_menu()
    if input_option == 1:
        book_dictionary = {}
        for i in ["title", "author", "publication date", "price", "readers"]:
            book_dictionary[i] = input("Please enter the " + i + " of the book: ")
        add_book_to_file("./BookShop.txt", book_dictionary.values())


main()
