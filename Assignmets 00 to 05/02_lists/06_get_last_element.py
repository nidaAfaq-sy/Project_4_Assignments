def get_last_element(lst):
    """Prints the last element of the provided list if the list is not empty."""
    if lst:
        print("Last Element:", lst[-1])
    else:
        print("The list is empty. No last element.")

def get_lst():
    """Prompts the user to enter elements one by one and returns the final list."""
    lst = []
    while True:
        elem = input("Please enter an element of the list or press Enter to stop: ")
        if elem == "":
            break
        lst.append(elem)
    return lst

def main():
    lst = get_lst()
    get_last_element(lst)

# Run the program
if __name__ == "__main__":
    main()
