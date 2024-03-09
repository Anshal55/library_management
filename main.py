from utils.inputs import user_input
from utils.operations import MenuOperation


def run_operation(choice: int) -> None:
    pass


def main():
    try:
        while True:
            choice: MenuOperation = user_input()
            print(f"Choice input: {choice}")

            if choice == 6:
                exit()

    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        main()


if __name__ == "__main__":
    main()
