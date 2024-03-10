from utils.operations import MenuOperation


class UserInputManagement:
    def __init__(self):
        pass

    def display_menu(self, options: list) -> int:
        """
        Display a menu with options and prompt the user for input.

        Args:
            options (list): List of menu options.

        Returns:
            int: User's choice.

        """
        while True:
            print("\n".join(options))
            try:
                choice = int(input("\nEnter your choice: "))
                if 1 <= choice <= len(options):
                    return choice
                else:
                    print("Invalid choice. Please enter a number within the range.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def user_input(self) -> MenuOperation:
        """
        Get user input for the main menu.

        Returns:
            MenuOperation: User's selected operation.

        """
        main_menu_options = [
            "\nMain menu (Enter a choice):",
            "1. Manage Books",
            "2. Manage Users",
            "3. Check-in/Check-out books",
            "4. Track book availability",
            "5. Exit"
        ]
        selection = self.display_menu(main_menu_options)

        if selection == 1:
            return self.manage_books()
        elif selection == 2:
            return self.manage_users()
        elif selection == 3:
            return self.check_in_out_books()
        elif selection == 4:
            return self.track_book_availability()
        elif selection == 5:
            return MenuOperation.EXIT_PROGRAM

    def manage_books(self) -> MenuOperation:
        """
        Get user input for the 'Manage Books' submenu.

        Returns:
            MenuOperation: User's selected operation in 'Manage Books'.

        """
        manage_books_options = [
            "\nManage Books (Enter a choice):",
            "1. Add books",
            "2. Update books",
            "3. Delete books",
            "4. List all books",
            "5. Search Books",
            "6. Back to previous menu"
        ]
        return MenuOperation(int(str(1) + str(self.display_menu(manage_books_options))))

    def manage_users(self) -> MenuOperation:
        """
        Get user input for the 'Manage Users' submenu.

        Returns:
            MenuOperation: User's selected operation in 'Manage Users'.

        """
        manage_users_options = [
            "\nManage Users (Enter a choice):",
            "1. Add users",
            "2. Update users",
            "3. Delete users",
            "4. List all users",
            "5. Search users",
            "6. Back to previous menu"
        ]
        return MenuOperation(int(str(2) + str(self.display_menu(manage_users_options))))

    def check_in_out_books(self) -> MenuOperation:
        """
        Get user input for the 'Check-in/Check-out books' submenu.

        Returns:
            MenuOperation: User's selected operation in 'Check-in/Check-out books'.

        """
        check_inout_books_options = [
            "\nCheck-in/Check-out books (Enter a choice):",
            "1. Check-in a book",
            "2. Check-out a book",
            "3. Back to previous menu"
        ]
        return MenuOperation(int(str(3) + str(self.display_menu(check_inout_books_options))))

    def track_book_availability(self) -> MenuOperation:
        """
        Get user input for the 'Track book availability' submenu.

        Returns:
            MenuOperation: User's selected operation in 'Track book availability'.

        """
        track_book_options = [
            "\nTrack book availability (Enter a choice):",
            "1. Track a book",
            "2. Back to previous menu"
        ]
        return MenuOperation(int(str(4) + str(self.display_menu(track_book_options))))

    def get_information(self) -> MenuOperation:
        """
        Get user input for the 'Get information' submenu.

        Returns:
            MenuOperation: User's selected operation in 'Get information'.

        """
        return MenuOperation.EXIT_PROGRAM


if __name__ == '__main__':
    ims = UserInputManagement()
    operation = ims.user_input()
    print(f"Operation selected: {operation}")
