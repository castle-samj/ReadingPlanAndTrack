# Class to define what an AUTHOR and BOOK objects would look like
import uuid


class Author:
    def __init__(self, nameFirst, nameLast):
        self.AuthorUID = uuid.uuid4()
        self.FirstName = nameFirst
        self.LastName = nameLast

class Book:
    def __init__(self, isbn, title, subtitle, author: Author, year):
        """isbn, title, subtitle, author, year"""
        self.BookUID = uuid.uuid4()
        self.ISBN = isbn
        self.Title = title
        self.Subtitle = subtitle
        self.Author = author
        self.Year = year

