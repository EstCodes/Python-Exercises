from uuid import uuid4

class Book:
    def __init__(self, title: str, author: str, isbn: int) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    def __init__(self) -> None:
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def removeBook(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def findBook(self, isbn) -> Book:
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def listBooks(self) -> list:
        for book in self.books:
            print(book)

# -------------------------------------------------------------------------------------------------

library = Library()

book1 = Book("Python: Basics", "Oreilly", "1721921728787")
book2 = Book("Java: Basics", "Oreilly", "8452989437787548")

library.addBook(book1 and book2)
library.listBooks()

library.removeBook(book1)
library.listBooks()

found_book = library.findBook("1721921728787")
if found_book:
    print("Founded: ", found_book)
else:
    print("Not found")