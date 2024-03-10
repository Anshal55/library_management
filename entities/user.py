class User:
    def __init__(self, name, user_id, book_isbns=None):
        """Initialize a User instance."""
        if book_isbns is None:
            book_isbns = []
        assert isinstance(name, str) and isinstance(user_id, str), "Invalid data types for User attributes."
        assert name and user_id, "Name and user ID are required."
        self.name = name
        self.user_id = user_id
        self.book_isbns = book_isbns or []

    def has_book(self, book_isbn: str) -> None:
        self.book_isbns.append(book_isbn)
