# file_handling_assignment.py

def create_and_write_file():
    try:
        # Create and open the file in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write three lines of text
            file.write("Hello, this is the first line.\n")
            file.write("This is the second line with a number: 12345.\n")
            file.write("Third line: Another example with the number 67890.\n")
        print("File created and initial content written successfully.")
    except PermissionError:
        print("Permission denied: unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Finished writing to the file.\n")


def read_file():
    try:
        # Open the file in read mode ('r')
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File content after reading:")
            print(content)
    except FileNotFoundError:
        print("File not found: make sure 'my_file.txt' exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Finished reading the file.\n")


def append_to_file():
    try:
        # Open the file in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text
            file.write("Appending a fourth line of text.\n")
            file.write("Appending the fifth line with a number: 54321.\n")
            file.write("Appending a sixth line: Final example 98765.\n")
        print("Additional content appended to the file successfully.")
    except PermissionError:
        print("Permission denied: unable to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Finished appending to the file.\n")


# Execute the functions
create_and_write_file()   # Step 1: Create the file and write initial content
read_file()               # Step 2: Read and display the file content
append_to_file()          # Step 3: Append additional content
read_file()               # Step 4: Read the updated content
