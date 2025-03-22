"""
Program: dice_simulator
----------------------
Simulates rolling two dice three times.
Demonstrates how variable scope works in Python.
"""

# Import the random library for generating random numbers
import random

# Number of sides on each die
NUM_SIDES = 6

def roll_and_print_dice():
    """
    Simulates rolling two dice and prints the result.
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Rolling dice... {die1} + {die2} = {total}")

def main():
    die1 = 10  # Local variable in main()
    print(f"Initial die1 in main(): {die1}")
    
    # Roll dice three times
    roll_and_print_dice()
    roll_and_print_dice()
    roll_and_print_dice()

    print(f"Final die1 in main(): {die1}")

# Entry point of the program
if __name__ == '__main__':
    main()
