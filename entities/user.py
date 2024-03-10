from dataclasses import dataclass
from typing import List


@dataclass
class User:
    name: str
    user_id: str
    book_isbns: List[str] = None

    def __post_init__(self):
        if self.book_isbns is None:
            self.book_isbns = []

    def has_book(self, book_isbn: str) -> None:
        self.book_isbns.append(book_isbn)
