from utils.operations import MenuOperation
from utils.inputs import UserInputManagement
from typing import Final

input_manager: Final[UserInputManagement] = UserInputManagement()


def run_operation(choice: int) -> None:
    pass


def main():
    try:
        while True:
            choice: MenuOperation = input_manager.user_input()
            print(f"Choice input: {choice}")

            if choice == MenuOperation.EXIT_PROGRAM:
                print("Thank you for using the LMS, See you!")
                exit()

    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        main()


if __name__ == "__main__":
    main()
