from dataclasses import dataclass
from typing import List


@dataclass
class Book:
    """
    Represents a book with a title, author, ISBN, and a flag indicating whether it is checked out.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The unique identifier (ISBN) of the book.
        checked_out (bool): A flag indicating whether the book is checked out.

    Example:
        book = Book(title="Introduction to Python", author="John Doe", isbn="978-0-385-08129-0")
    """

    title: str
    author: str
    isbn: str
    checked_out: bool = False
