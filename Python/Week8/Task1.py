#Author - Book (note: association)

class Author:
    def __init__(self, firstname, surename):
        self.firstname = firstname
        self.surename = surename
        self.book = None
    
    def addBook(self, newBook):
        self.book = newBook
    
    def getAuthor(self):
        authorInfo = "Author: " + self.firstname + " " + self.surename
        return authorInfo
    
class Book:
    def __init__(self, name, year, pages, bookType, isbn):
        self.name = name
        self.year = year
        self.pages = pages
        self.bookType = bookType
        self.isbn = isbn

    def returnBookInfo(self):
        bookInfo = "Name: " + self.name
        bookInfo += "\nYear: " + str(self.year)
        bookInfo += "\nPages: " + str(self.pages)
        bookInfo += "\nFormat: " + self.bookType
        bookInfo += "\nISBN: " + self.isbn
        return bookInfo


author1 = Author("Andriy", "Burkov")
book1 = Book("The Hudred-page Machine Learning Book", 2019, 160, "Paperback", "978-1999579500")
author1.addBook(book1)

print(author1.getAuthor())
print(author1.book.returnBookInfo())
