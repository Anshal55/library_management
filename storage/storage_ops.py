import json
import os

DATA_FILE_PATH = '../data/library_data.json'


def load_data():
    """Load data from file."""

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(DATA_FILE_PATH), exist_ok=True)

    try:
        with open(DATA_FILE_PATH, 'r') as file:
            # Check if the file is empty before trying to load its content
            if os.path.getsize(DATA_FILE_PATH) > 0:
                data = json.load(file)
            else:
                data = {}
    except FileNotFoundError:
        data = {}

    return data


def save_data_to_file(data):
    """Save data to file."""
    with open(DATA_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    json = load_data()
