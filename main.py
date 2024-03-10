from utils.operations import MenuOperation
from utils.inputs import UserInputManagement
from library.library_manager import perform_operation
from library.library_class import Library
from typing import Final
from utils.logger import logging

logger: Final = logging.getLogger("Main Loop")

# Instantiate user input object and library object here
INPUT_MANAGER: Final[UserInputManagement] = UserInputManagement()
LIBRARY: Final[Library] = Library()


# Main function loop to act as the LMS start and end point
def main():
    try:
        while True:
            try:
                print("\n\n** LIBRARY MANAGEMENT SYSTEM **")
                choice: MenuOperation = INPUT_MANAGER.user_input()

                if choice == MenuOperation.EXIT_PROGRAM:
                    logger.info("Thank you for using the LMS. See you!")
                    break

                # Pass the required operation to the function to be performed
                op_completed: bool = perform_operation(LIBRARY, choice)

            except Exception as e:
                logger.error(f"An error occurred: {str(e)}")
                # Continue with the next iteration of the loop

    except KeyboardInterrupt:
        logger.error("User interrupted. Exiting the LMS.")

    finally:
        logger.info("Exiting the LMS.")
        LIBRARY.save_data()


if __name__ == "__main__":
    main()
