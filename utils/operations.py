from enum import Enum


class MenuOperation(Enum):
    """
    Represents different operations available in the library management system.
    """

    # Book Management
    ADD_BOOKS = 11
    UPDATE_BOOKS = 12
    DELETE_BOOKS = 13
    LIST_BOOKS = 14
    SEARCH_BOOKS = 15
    PREVIOUS_MENU_BOOKS = 16  # Option to go back to previous menu from Book Management

    # User Management
    ADD_USERS = 21
    UPDATE_USERS = 22
    DELETE_USERS = 23
    LIST_USERS = 24
    SEARCH_USERS = 25
    PREVIOUS_MENU_USERS = 26  # Option to go back to previous menu from User Management

    # Check-in/Out and Tracking
    CHECK_IN_BOOK = 31
    CHECK_OUT_BOOK = 32
    PREVIOUS_MENU_CHECK_IN_OUT = 33  # Option to go back to previous menu from Check-in/Out

    # Track Book
    TRACK_BOOK = 41
    PREVIOUS_MENU_TRACK_BOOK = 42  # Option to go back to previous menu from Track Book

    # Information
    GET_INFO = 51
    PREVIOUS_MENU_INFO = 52  # Option to go back to previous menu from Information


if __name__ == '__main__':
    # Accessing operations by name
    selected_operation = MenuOperation.ADD_BOOKS
    print(selected_operation.name)  # Output: ADD_BOOKS

    # Accessing operation value (integer)
    operation_value = MenuOperation.CHECK_OUT_BOOK.value
    print(operation_value)  # Output: 32
