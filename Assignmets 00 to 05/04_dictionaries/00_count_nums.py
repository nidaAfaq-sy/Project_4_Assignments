from collections import defaultdict

def get_user_numbers():
    """
    Ask the user to input numbers and store them in a list. 
    Stop when a blank line is entered.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        
        if user_input == "":
            break
        
        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    return user_numbers

def count_nums(num_lst):
    """
    Count occurrences of each number using a dictionary.
    """
    num_dict = defaultdict(int)
    for num in num_lst:
        num_dict[num] += 1
    
    return num_dict

def print_counts(num_dict):
    """
    Print each number and its count.
    """
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")

def main():
    """
    Get user numbers, count occurrences, and display results.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == '__main__':
    main()
