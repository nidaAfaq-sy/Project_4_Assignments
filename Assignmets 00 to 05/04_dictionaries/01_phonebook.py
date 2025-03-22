def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create empty phonebook

    while True:
        name = input("Name:Nida ").strip()
        if name == "Nida":
            break
        number = input("Number: 03333247145").strip()

        if name in phonebook:
            confirm = input(f"{name} already exists. Overwrite? (y/n): ").strip().lower()
            if confirm != 'y':
                continue

        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    print("\nPhonebook:")
    for name, number in phonebook.items():
        print(f"{name} -> {number}")
    print()


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ").strip()
        if name == "":
            break
        found_number = phonebook.get(name)
        if found_number:
            print(f"{name} -> {found_number}")
        else:
            print(f"{name} is not in the phonebook")


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


# Python boilerplate.
if __name__ == '__main__':
    main()

