# file_handling_assignment.py

def create_file():
    try:
        # Creating a new text file named "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Writing at least three lines of text to the file, including a mix of strings and numbers
            file.write("Hello, this is the first line.\n")
            file.write("The number 42 is meaningful in some contexts.\n")
            file.write("Python file handling is interesting!\n")
        print("File created and initial content written successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file():
    try:
        # Reading the contents of "my_file.txt" and displaying them on the console
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Current contents of the file:")
            print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied while trying to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

def append_to_file():
    try:
        # Opening "my_file.txt" in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Appending three additional lines of text to the existing content
            file.write("Appending a fourth line to the file.\n")
            file.write("Another line with the number 2024.\n")
            file.write("This is the final appended line.\n")
        print("Additional content appended successfully.")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied while trying to append to the file.")
    except Exception as e:
        print(f"An unexpected error occurred while appending to the file: {e}")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read the file again to display the updated contents

if __name__ == "__main__":
    main()
