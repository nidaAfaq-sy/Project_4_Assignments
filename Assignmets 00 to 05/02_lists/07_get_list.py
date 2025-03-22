def main():
    lst = []  # Create an empty list

    while True:
        val = input("Enter a value (press Enter to stop): ")  # Get input
        if val == "":  # Stop if input is empty
            break
        lst.append(val)  # Add value to list

    print("Here's the list:", lst)  # Print the list

# No need to edit beyond this point
if __name__ == '__main__':
    main()
