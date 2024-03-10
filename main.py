from utils.operations import MenuOperation
from utils.inputs import UserInputManagement
from library.library_manager import perform_operation
from library.library_class import Library
from typing import Final

# Instantiate user input object and library object here
INPUT_MANAGER: Final[UserInputManagement] = UserInputManagement()
LIBRARY: Final[Library] = Library()


# Main function loop to act as the LMS start and end point
def main():
    try:
        while True:
            choice: MenuOperation = INPUT_MANAGER.user_input()

            if choice == MenuOperation.EXIT_PROGRAM:
                print("Thank you for using the LMS. See you!")
                break

            print(f"Input from user: {choice}")

            # Pass the required operation to the function to be performed
            op_completed: bool = perform_operation(LIBRARY, choice)

    except KeyboardInterrupt:
        print("\nUser interrupted. Exiting the LMS.")

    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

    finally:
        print("Exiting the LMS.")


if __name__ == "__main__":
    main()
