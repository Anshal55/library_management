from utils.operations import MenuOperation


def user_input() -> MenuOperation:
    while True:
        print("\nLibrary Management System\n"
              "1. Manage Books\n2. Manage Users\n3. Check-in/ Check-out books\n"
              "4. Track book availability\n5. Get information\n6. Exit")

        try:
            selection = int(input("\nEnter your choice (1/2/3/4/5/6): "))
            if 1 <= selection <= 6:
                break
            else:
                print("Invalid selection. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    run_operation = MenuOperation.PREVIOUS_MENU_USERS

    if selection == 1:
        run_operation = manage_books(selection)
    elif selection == 2:
        run_operation = manage_users(selection)
    elif selection == 3:
        run_operation = check_in_out_books(selection)
    elif selection == 4:
        run_operation = track_book_availability(selection)
    elif selection == 5:
        get_information()
    elif selection == 6:
        exit_system()

    return run_operation


def manage_books(choice: int) -> MenuOperation:
    while True:
        print("\n1. Add books\n2. Update books\n3. Delete books\n"
              "4. List all books\n5. Search Books\n6. Back to previous menu")
        manage_book_choice = None

        try:
            manage_book_choice = int(input("\nEnter your choice (1/2/3/4/5/6): "))
            if 1 <= manage_book_choice <= 6:
                break
            else:
                print("Invalid choice. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        if manage_book_choice == 6:
            return user_input()

    return MenuOperation(int(str(choice) + str(manage_book_choice)))


def manage_users(choice: int) -> MenuOperation:
    while True:
        print("\n1. Add users\n2. Update users\n3. Delete users\n"
              "4. List all users\n5. Search users\n6. Back to previous menu")
        manage_user_choice = None

        try:
            manage_user_choice = int(input("\nEnter your choice (1/2/3/4/5/6): "))
            if 1 <= manage_user_choice <= 6:
                break
            else:
                print("Invalid choice. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        if manage_user_choice == 6:
            return user_input()

    return MenuOperation(int(str(choice) + str(manage_user_choice)))


def check_in_out_books(choice: int) -> MenuOperation:
    while True:
        print("\n1. Check-in a book\n2. Check-out a book\n3. Back to previous menu")
        check_inout_choice = None

        try:
            check_inout_choice = int(input("\nEnter your choice (1/2/3): "))
            if 1 <= check_inout_choice <= 3:
                break
            else:
                print("Invalid choice. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        if check_inout_choice == 3:
            return user_input()

    return MenuOperation(int(str(choice) + str(check_inout_choice)))


def track_book_availability(choice: int) -> MenuOperation:
    while True:
        print("\n1. Track a book\n2. Back to previous menu")
        tracking_choice = None

        try:
            tracking_choice = int(input("\nEnter your choice (1/2): "))
            if 1 <= tracking_choice <= 2:
                break
            else:
                print("Invalid choice. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        if tracking_choice == 2:
            return user_input()

    return MenuOperation(int(str(choice) + str(tracking_choice)))


def get_information():
    print("Get book information.")


def exit_system():
    print("Thanks for using the LMS.")
    exit()


if __name__ == '__main__':
    operation = user_input()
    print(f"Operation selected: {operation}")
