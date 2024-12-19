def read_and_modify_file():
    try:
        # askking the user to enter file name
        input_filename = input("Enter the filename to read from: ")
        
        # oppenning and reading the user's file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        # modified to uppercase
        modified_content = content.upper()

        # Asking user for the name of the seconf file to copy the modified version
        output_filename = input("Enter the new filename to save the modified content: ")
        
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist. Please try again.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# calling the function
read_and_modify_file()
