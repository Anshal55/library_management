from dataclasses import dataclass
from typing import List


@dataclass
class User:
    """
    Represents a library user with a name, user ID, and a list of ISBNs of checked-out books.

    Attributes:
        name (str): The name of the user.
        user_id (str): The unique identifier of the user.
        book_isbns (List[str]): A list containing ISBNs of books checked out by the user.

    Methods: __post_init__(self): Initializes the 'book_isbns' attribute to an empty list if it is not provided
    during instantiation. has_book(self, book_isbn: str) -> None: Adds the provided book ISBN to the user's list of
    checked-out books.

    Example:
        user = User(name="John Doe", user_id="123")
        user.has_book("978-0-385-08129-0")
    """

    name: str
    user_id: str
    book_isbns: List[str] = None

    def __post_init__(self):
        """
        Initializes the 'book_isbns' attribute to an empty list if it is not provided during instantiation.
        """
        if self.book_isbns is None:
            self.book_isbns = []

    def has_book(self, book_isbn: str) -> None:
        """
        Adds the provided book ISBN to the user's list of checked-out books.

        Args:
            book_isbn (str): The ISBN of the book to be added to the user's list.
        """
        self.book_isbns.append(book_isbn)
