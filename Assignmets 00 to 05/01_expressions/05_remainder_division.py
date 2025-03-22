def main():
    # Get the numbers we want to divide
    dividend = int(input("Enter the dividend (integer): "))
    divisor = int(input("Enter the divisor (integer): "))
    
    # Perform division
    quotient = dividend // divisor  # Integer division
    remainder = dividend % divisor  # Modulo operation
    
    # Display results
    print(f"{dividend} divided by {divisor} gives quotient {quotient} and remainder {remainder}.")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
