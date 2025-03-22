MAX_LENGTH: int = 3

def shorten(lst):
    """
    Removes elements from the list until its length is MAX_LENGTH.
    Prints each removed element.
    """
    while len(lst) > MAX_LENGTH:
        print("Removing:", lst.pop())

def get_lst():
    """
    Prompts the user to enter elements one at a time and returns the list.
    """
    lst = []
    while True:
        elem = input("Enter an element (or press Enter to stop): ")
        if not elem:
            break
        lst.append(elem)
    return lst

def main():
    lst = get_lst()
    shorten(lst)
    print("Final list:", lst)

if __name__ == '__main__':
    main()
