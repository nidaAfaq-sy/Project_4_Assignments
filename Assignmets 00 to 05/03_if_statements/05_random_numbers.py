import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    Generates a list of random numbers and prints them.
    Also calculates and prints the sum and average of the numbers.
    """
    numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    
    total = sum(numbers)
    average = total / N_NUMBERS

    print(f"Generated numbers: {numbers}")
    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")

if __name__ == '__main__':
    main()
