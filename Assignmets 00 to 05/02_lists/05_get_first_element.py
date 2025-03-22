def get_first_element(lst):
    """
    Prints the first element of a provided list, if available.
    """
    if lst:
        print(f"First element: {lst[0]}")
    else:
        print("The list is empty. No first element to display.")

# No changes needed beyond this point

def get_lst():
    """
    Prompts the user to enter elements one at a time and returns the resulting list.
    """
    lst = []
    elem = input("Enter an element (or press Enter to finish): ")
    while elem:
        lst.append(elem)
        elem = input("Enter another element (or press Enter to finish): ")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)

if __name__ == '__main__':
    main()
