from dataclasses import dataclass
from typing import List


@dataclass
class Book:
    title: str
    author: str
    isbn: str
    checked_out: bool = False
