# file_handling_assignment.py

import os
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class FileHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def create_and_write_file(self, content):
        """Creates a file and writes the provided content to it."""
        try:
            with open(self.file_name, 'w') as file:
                file.writelines(content)
            logging.info(f"File '{self.file_name}' created and content written.")
        except PermissionError:
            logging.error("Permission denied: unable to write to the file.")
        except Exception as e:
            logging.error(f"An error occurred while writing to the file: {e}")
        finally:
            logging.info("Write operation completed.")

    def read_file(self):
        """Reads and prints the content of the file."""
        if not os.path.exists(self.file_name):
            logging.warning(f"File '{self.file_name}' does not exist.")
            return None

        try:
            with open(self.file_name, 'r') as file:
                content = file.read()
                logging.info("File content read successfully.")
                return content
        except FileNotFoundError:
            logging.error(f"File '{self.file_name}' not found.")
        except Exception as e:
            logging.error(f"An error occurred while reading the file: {e}")
        finally:
            logging.info("Read operation completed.")

    def append_to_file(self, additional_content):
        """Appends new content to the file."""
        try:
            with open(self.file_name, 'a') as file:
                file.writelines(additional_content)
            logging.info(f"New content appended to '{self.file_name}'.")
        except PermissionError:
            logging.error("Permission denied: unable to append to the file.")
        except Exception as e:
            logging.error(f"An error occurred while appending to the file: {e}")
        finally:
            logging.info("Append operation completed.")


# Example usage
if __name__ == "__main__":
    file_name = "my_file.txt"
    handler = FileHandler(file_name)

    # Step 1: Create file and write content
    initial_content = [
        "Hello, this is the first line.\n",
        "This is the second line with a number: 12345.\n",
        "Third line: Another example with the number 67890.\n"
    ]
    handler.create_and_write_file(initial_content)

    # Step 2: Read and display the file content
    content = handler.read_file()
    if content:
        logging.info(f"Current file content:\n{content}")

    # Step 3: Append more content
    additional_content = [
        "Appending a fourth line of text.\n",
        "Appending the fifth line with a number: 54321.\n",
        "Appending a sixth line: Final example 98765.\n"
    ]
    handler.append_to_file(additional_content)

    # Step 4: Read the updated file content
    updated_content = handler.read_file()
    if updated_content:
        logging.info(f"Updated file content:\n{updated_content}")
