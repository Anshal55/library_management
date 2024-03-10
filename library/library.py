from entities.book import Book
from entities.user import User
from storage.storage_ops import load_data, save_data_to_file
from uuid import uuid4


class Library:
    def __init__(self):
        """Initialize the Library."""
        self.books = {}
        self.users = {}
        self.load_data()

    def load_data(self):
        """Load data from storage."""
        data = load_data()
        self.books = {isbn: Book(**book_data) for isbn, book_data in data.get('books', {}).items()}
        self.users = {user_id: User(**user_data) for user_id, user_data in data.get('users', {}).items()}

    def save_data(self):
        """Save data to storage."""
        data = {
            'books': {
                isbn: {'title': book.title, 'author': book.author, 'isbn': book.isbn, 'checked_out': book.checked_out}
                for isbn, book in self.books.items()},
            'users': {user_id: {'name': user.name, 'user_id': user.user_id, 'book_isbns': user.book_isbns}
                      for user_id, user in self.users.items()}
        }

        save_data_to_file(data)

    def add_book(self, title, author, isbn=None):
        """Add a new book to the library."""
        assert isinstance(title, str) and isinstance(author, str), "Invalid data types for Book attributes."
        assert title and author, "Title and author are required."

        if isbn is None:
            isbn = str(uuid4())  # Generate a UUID as the ISBN if not provided

        new_book = Book(title, author, isbn)
        self.books[isbn] = new_book
        self.save_data()

    def list_books(self):
        """List all books in the library."""
        if not self.books:
            print("No books available in the library.")
            return

        for book in self.books.values():
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")

    def delete_book(self, isbn):
        """Delete a book from the library based on ISBN."""
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} has been deleted.")
            self.save_data()
        else:
            print(f"No book found with ISBN {isbn}.")

    def update_book(self, isbn, **attributes):
        """Update book information based on ISBN."""
        if isbn in self.books:
            book = self.books[isbn]
            for key, value in attributes.items():
                setattr(book, key, value)
            print(f"Book with ISBN {isbn} has been updated.")
            self.save_data()
        else:
            print(f"No book found with ISBN {isbn}.")

    def search_books(self, **attributes):
        """Search for books based on given attributes."""
        if not attributes:
            print("Please provide at least one attribute to search for.")
            return

        found_books = []
        for book in self.books.values():
            if all(getattr(book, key, None) == value for key, value in attributes.items()):
                found_books.append(book)

        if not found_books:
            print("No books found with the specified attributes.")
            return

        for found_book in found_books:
            print(f"Title: {found_book.title}, Author: {found_book.author}, ISBN: {found_book.isbn}")

    # Implement other book management methods (update, delete, checkout, check-in, availability)

    def add_user(self, name, user_id=None):
        """Add a new user to the library."""
        assert isinstance(name, str), "Invalid data types for User attributes."
        assert name, "Name is required."

        if user_id is None:
            user_id = str(uuid4())  # Generate a UUID as the user_id if not provided

        new_user = User(name, user_id)
        self.users[user_id] = new_user
        self.save_data()

    def list_users(self):
        """List all users in the library."""
        if not self.users:
            print("No users registered in the library.")
            return

        for user in self.users.values():
            print(f"Name: {user.name}, User ID: {user.user_id}")

    def delete_user(self, user_id):
        """Delete a user from the library based on user ID."""
        if user_id in self.users:
            del self.users[user_id]
            print(f"User with ID {user_id} has been deleted.")
            self.save_data()
        else:
            print(f"No user found with ID {user_id}.")

    def update_user(self, user_id, **attributes):
        """Update user information based on user ID."""
        if user_id in self.users:
            user = self.users[user_id]
            for key, value in attributes.items():
                setattr(user, key, value)
            print(f"User with ID {user_id} has been updated.")
            self.save_data()
        else:
            print(f"No user found with ID {user_id}.")

    def check_out_book(self, user_id, isbn):
        """Check out a book to a user."""
        if user_id in self.users and isbn in self.books:
            user = self.users[user_id]
            book = self.books[isbn]

            if not book.checked_out:
                user.book_isbns.append(isbn)
                book.checked_out = True
                print(f"Book with ISBN {isbn} has been checked out to user {user_id}.")
            else:
                print(f"Book with ISBN {isbn} is already checked out.")
        else:
            print(f"No user found with ID {user_id} or no book found with ISBN {isbn}.")

    def check_in_book(self, user_id, isbn):
        """Check in a book from user."""
        if user_id in self.users and isbn in self.books:
            user = self.users[user_id]
            book = self.books[isbn]

            if isbn in user.book_isbns:
                user.book_isbns.remove(isbn)
                book.checked_out = False
                print(f"Book with ISBN {isbn} has been checked in from user {user_id}.")
            else:
                print(f"Book with ISBN {isbn} is not checked out to user {user_id}.")
        else:
            print(f"No user found with ID {user_id} or no book found with ISBN {isbn}.")

    def track_book(self, book_isbn: str) -> bool:
        is_available = False

        if book_isbn in self.books:
            book = self.books[book_isbn]

            if not book.checked_out:
                is_available = True

        return is_available


if __name__ == '__main__':
    l1 = Library()
    l1.add_book("Anne of Green Gables", "XYZ", "AGG")
    l1.add_book("Harry Potter", "J.K. Rowling", "HP")
    l1.list_books()

    # Example of searching by title
    print("\nSearching by title:")
    l1.search_books(title="Anne of Green Gables")

    # Example of searching by author
    print("\nSearching by author:")
    l1.search_books(author="J.K. Rowling")

    # Example of searching by ISBN
    print("\nSearching by ISBN:")
    l1.search_books(isbn="0-12345-7654")

    l1.add_user("Anshal", "A123")
    l1.add_user("Jack", "J123")

    l1.delete_user("A123")
    l1.delete_book("HP")

    l1.add_book("The Great Gatsby", "F. Scott Fitzgerald", "TGG")
    l1.add_user("John Doe", "J123")
    l1.check_out_book("J123", "TGG")  # Replace "generated_isbn" with the actual ISBN
    l1.list_books()
    l1.list_users()
    # l1.check_in_book("J123", "TGG")
    l1.list_books()
    l1.list_users()

    print(f"Is book available = {l1.track_book('TGG')}")

    l1.save_data()
