# Author: Vinit Kirit Jain
# Assignment: Lab 8
# Date: 2023-10-25


class Book:
    discount = 0

    def __init__(self, title, pages, author, price):
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price

    def setDiscount(self, amount):
        self.discount = amount

    def getPrice(self):
        return self.price

    def setDiscount(self, percentage):
        self.discount = percentage / 100

    def getPriceAfterDiscount(self):
        return self.price * (1.0 - self.discount)


# Q1: create 3 books with title, pages, author, and price

# creating three book objects and specifying their attribute values
book1 = Book(
    "The Lord of the Rings: The Fellowship of the Ring",
    576,
    "J.R.R. Tolkien",
    11.15,
)
book2 = Book(
    "Harry Potter and the Sorcerer's Stone",
    333,
    "J.K. Rowling",
    12.99,
)
book3 = Book(
    "To Kill a Mockingbird",
    324,
    "Harper Lee",
    10.99,
)

# storing all the book object in a list for east access
book_list = [book1, book2, book3]

# Q2: print the price of all three books
# iterating through the book list and printing the price
for i in book_list:
    print(str(i.price))

# Q3: create class function - getPriceAfterDiscount(self): which returns the price after discount
# With iteration we set the discount percentage and then calculate the price after discount and print to the user
for i in book_list:
    i.setDiscount(25)
    print(i.getPriceAfterDiscount())

# Q4: set discounts for the 3 books, print the the price before and after

print("Q4")
# In each iteration we are setting the discount at 25 percent and printing the before and after the discount price of each book
for i in book_list:
    i.setDiscount(25)
    print(
        i.title
        + "; "
        + "Before discount: "
        + str(i.price)
        + "; After discount: "
        + str(i.getPriceAfterDiscount())
    )

# Q5: Create another class store, with attributes books, storeName, where books is a list.


# creating a new class for store which has two attributes
class Store:
    def __init__(self, books, storeName):
        self.books = books
        self.storeName = storeName


# Q6: Create instance of store, append all books to store.books and then print all the prices of the stores books.

print("Q6")
# setting our previous book list as store attribute as well as the name of the store and creating a store object
store1 = Store(book_list, "Amazon")

# iterating through the list of the books using the store object and printing their price
for i in store1.books:
    print(str(i.price))
