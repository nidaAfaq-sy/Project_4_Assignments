def add_three_copies(my_list, data):
    my_list.extend([data] * 3)  # For loop ki jagah ek line me kaam ho gaya

########## No need to edit code past this point

def main():
    message = input("Enter a message to copy: ")
    my_list = []
    
    print(f"List before adding copies: {my_list}")  # Output ko thoda improve kiya
    add_three_copies(my_list, message)
    print(f"List after adding copies: {my_list}")

if __name__ == "__main__":
    main()
