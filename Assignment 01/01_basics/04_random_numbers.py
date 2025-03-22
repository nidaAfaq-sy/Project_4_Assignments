import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    Generates and prints N_NUMBERS random integers between MIN_VALUE and MAX_VALUE.
    """
    random_numbers = random.sample(range(MIN_VALUE, MAX_VALUE + 1), N_NUMBERS)
    print("Generated Numbers:", ", ".join(map(str, random_numbers)))

if __name__ == '__main__':
    main()
