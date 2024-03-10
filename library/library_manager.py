from library.library_class import Library
from utils.operations import MenuOperation


def perform_operation(library: Library, user_input_op: MenuOperation) -> bool:
    """
    Perform the library operation based on user input.

    Args:
       user_input_op (MenuOperation): The user input representing the selected operation.
       library (Library): Clas instance of Library

    Returns:
       bool: True if the operation was successful, False otherwise.
    """

    match user_input_op:
        case MenuOperation.ADD_BOOKS:
            library.add_book(*get_book_details())
        case MenuOperation.UPDATE_BOOKS:
            isbn, attributes = get_book_update_details()
            library.update_book(isbn, **attributes)
        case MenuOperation.DELETE_BOOKS:
            library.delete_book(get_book_delete_details())
        case MenuOperation.LIST_BOOKS:
            library.list_books()
        case MenuOperation.SEARCH_BOOKS:
            library.search_books(**get_book_search_details())
        case MenuOperation.ADD_USERS:
            library.add_user(*get_user_details())
        case MenuOperation.UPDATE_USERS:
            user_id, attributes = get_user_update_details()
            library.update_user(user_id, **attributes)
        case MenuOperation.DELETE_USERS:
            library.delete_user(get_user_delete_details())
        case MenuOperation.LIST_USERS:
            library.list_users()
        case MenuOperation.SEARCH_USERS:
            library.search_users(**get_user_search_details())
        case MenuOperation.CHECK_OUT_BOOK:
            library.check_out_book(*get_check_out_details())
        case MenuOperation.CHECK_IN_BOOK:
            library.check_in_book(*get_check_in_details())
        case MenuOperation.TRACK_BOOK:
            library.track_book(get_book_isbn())
        case MenuOperation.GET_INFO:
            print("Not Implemented")
        case _:
            print("Unexpected input")

    return True


def get_book_details() -> list[str]:
    book_name = input("Enter book name: ")
    author_name = input("Enter author name: ")
    isbn_value = input("Enter ISBN: ")

    assert isinstance(book_name, str) and book_name, "Book name has to be a non-empty string"
    assert isinstance(author_name, str) and author_name, "Author name has to be a non-empty string"
    assert isinstance(isbn_value, str) and isbn_value, "ISBN value has to be a non-empty string"

    return [book_name, author_name, isbn_value]


def get_book_update_details() -> [str, dict]:
    isbn_value = input("Enter ISBN: ")
    assert isinstance(isbn_value, str) and isbn_value, "ISBN value has to be a non-empty string"

    book_name = input("Enter book name (Press Enter to skip): ")
    author_name = input("Enter author name (Press Enter to skip): ")
    assert isinstance(book_name, str), "Book name has to be a string"
    assert isinstance(author_name, str), "Author name has to be a string"

    details = {
        "title": book_name.strip() if book_name else None,
        "author": author_name.strip() if author_name else None,
    }

    # Remove empty values from the dictionary
    details = {key: value for key, value in details.items() if value is not None}

    return isbn_value, details


def get_book_delete_details() -> str:
    isbn_value = input("Enter ISBN: ")

    assert isinstance(isbn_value, str) and isbn_value, "ISBN value has to be a non-empty string"

    return isbn_value


def get_book_search_details() -> dict:
    isbn_value = input("Enter ISBN (Press Enter to skip): ")
    book_name = input("Enter book name (Press Enter to skip): ")
    author_name = input("Enter author name (Press Enter to skip): ")

    assert isinstance(isbn_value, str), "ISBN value has to be a string"
    assert isinstance(book_name, str), "Book name has to be a string"
    assert isinstance(author_name, str), "Author name has to be a string"

    details = {
        "title": book_name.strip() if book_name else None,
        "author": author_name.strip() if author_name else None,
        "isbn": isbn_value.strip() if isbn_value else None,
    }

    # Remove empty values from the dictionary
    details = {key: value for key, value in details.items() if value is not None}

    assert (len(details.keys()) > 0), "Please input at-least one value"

    return details


def get_user_details() -> list[str]:
    user_name = input("Enter name: ")
    user_id = input("Enter id: ")

    assert isinstance(user_name, str) and user_name, "Name has to be a non-empty string"
    assert isinstance(user_id, str) and user_id, "ID has to be a non-empty string"

    return [user_name, user_id]


def get_user_update_details() -> [str, dict]:
    user_id = input("Enter UserID: ")
    assert isinstance(user_id, str) and user_id, "UserID value has to be a non-empty string"

    user_name = input("Enter Name (Press Enter to skip): ")
    assert isinstance(user_name, str), "Name has to be a string"

    details = {
        "name": user_name.strip() if user_name else None,
    }

    # Remove empty values from the dictionary
    details = {key: value for key, value in details.items() if value is not None}

    return user_id, details


def get_user_delete_details() -> str:
    id_value = input("Enter UserID: ")

    assert isinstance(id_value, str) and id_value, "UserID value has to be a non-empty string"

    return id_value


def get_user_search_details() -> dict:
    name = input("Enter Name (Press Enter to skip): ")
    user_id = input("Enter UserID (Press Enter to skip): ")

    assert isinstance(user_id, str), "Name value has to be a string"
    assert isinstance(name, str), "UserID name has to be a string"

    details = {
        "name": name.strip() if name else None,
        "user_id": user_id.strip() if user_id else None,
    }

    # Remove empty values from the dictionary
    details = {key: value for key, value in details.items() if value is not None}

    assert (len(details.keys()) > 0), "Please input at-least one value"

    return details


def get_check_out_details() -> list[str]:
    book_isbn = input("Enter Book ISBN (Press Enter to skip): ")
    user_id = input("Enter UserID (Press Enter to skip): ")

    assert isinstance(book_isbn, str) and book_isbn, "Name value has to be a non-empty string"
    assert isinstance(user_id, str) and user_id, "UserID name has to be a non-empty string"

    return [user_id, book_isbn]


def get_check_in_details() -> list[str]:
    book_isbn = input("Enter Book ISBN (Press Enter to skip): ")
    user_id = input("Enter UserID (Press Enter to skip): ")

    assert isinstance(book_isbn, str) and book_isbn, "Name value has to be a non-empty string"
    assert isinstance(user_id, str) and user_id, "UserID name has to be a non-empty string"

    return [user_id, book_isbn]


def get_book_isbn() -> str:
    book_isbn = input("Enter Book ISBN (Press Enter to skip): ")
    assert isinstance(book_isbn, str) and book_isbn, "Name value has to be a non-empty string"

    return book_isbn


if __name__ == '__main__':
    lib = Library()
    lib.list_books()
    lib.list_users()

    op_name = MenuOperation.TRACK_BOOK

    perform_operation(lib, op_name)

    lib.list_users()

    lib.save_data()
