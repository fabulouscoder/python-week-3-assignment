def read_and_modify_file():
    try:
        # Ask user for the input file name
        filename = input("Enter the name of the file to read: ")

        # Open and read the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify content (for demo: convert text to uppercase)
        modified_content = content.upper()

        # Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"File processed successfully! Modified file saved as '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# Run the function
if __name__ == "__main__":
    read_and_modify_file()
