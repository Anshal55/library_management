# Library Management System (LMS)

The Library Management System (LMS) is a simple yet powerful library management application. It provides functionality to manage books, users, and book borrowing operations. The system employs a singleton pattern to ensure a single instance of the library is created.

## Table of Contents

- [Library Management System (LMS)](#library-management-system-lms)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Usage](#usage)
  - [File Structure](#file-structure)
    - [Folder Structure](#folder-structure)
    - [TODO:](#todo)

## Features

- **Add Books:** Add new books to the library with details such as title, author, and ISBN.
- **List Books:** Display a list of all books available in the library.
- **Delete Books:** Remove a book from the library based on its ISBN.
- **Update Books:** Modify book information such as title and author based on ISBN.
- **Search Books:** Search for books using various attributes like title, author, and ISBN.
- **Add Users:** Register new users in the library with details like name and user ID.
- **List Users:** View a list of all registered users in the library.
- **Delete Users:** Remove a user from the library based on their user ID.
- **Update Users:** Modify user information such as name based on user ID.
- **Search Users:** Search for users using attributes like name and user ID.
- **Check Out Books:** Allow users to borrow books from the library.
- **Check In Books:** Enable users to return borrowed books to the library.
- **Track Book Availability:** Check whether a book is available for borrowing based on ISBN.

## Usage

1. **Installation:**

   ```bash
   pip3 install coloredlogs
   ```

2. **Python Version:**
   
   Ensure you have Python version 3.10 or higher installed.

3. **Run the program:**

   ```bash
   python3 main.py
   ```

## File Structure

```shell
.
├── data
│   └── library_data.json
├── entities
│   ├── book.py
│   ├── __init__.py
│   └── user.py
├── library
│   ├── __init__.py
│   ├── library_class.py
│   ├── library_manager.py
├── main.py
├── README.md
├── storage
│   ├── __init__.py
│   └── storage_ops.py
└── utils
    ├── __init__.py
    ├── inputs.py
    ├── logger.py
    ├── operations.py
```

### Folder Structure

- **data:**
  Holds the file or data that contains information about books and users.

- **entities:**
  Defines the structure of books and users.

- **library:**
  Contains the Library class and its methods. Also includes the library manager responsible for running operations based on user selection.

- **storage:**
  Implements file I/O operations for saving and loading data.

- **utils:**
  Holds utilities such as logger, input handling, and mapping inputs to fixed operations.

- **main.py:**
  Serves as the start and end point for invoking the Library Management System.


### TODO:
1. Improve the structure further.
2. Can use database in place of file.
3. Can introduce UI for management.