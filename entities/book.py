# class Book:
#     def __init__(self, title, author, isbn, checked_out=False):
#         """Initialize a Book instance."""
#         assert isinstance(title, str) and isinstance(author, str) and isinstance(isbn,
#                                                                                  str), ("Invalid data types for Book "
#                                                                                         "attributes.")
#         assert title and author and isbn, "Title, author, and ISBN are required."
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.checked_out = checked_out

from dataclasses import dataclass
from typing import List


@dataclass
class Book:
    title: str
    author: str
    isbn: str
    checked_out: bool = False
