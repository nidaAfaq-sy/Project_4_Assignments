"""
Simulates rolling two dice and prints the results of each roll along with the total.
"""

import random

# Number of sides on each die
NUM_SIDES = 6

def roll_die(sides: int) -> int:
    """Simulates rolling a die with the given number of sides."""
    return random.randint(1, sides)

def main():
    # Uncomment to set a seed for debugging
    # random.seed(1)
    
    # Roll two dice
    die1 = roll_die(NUM_SIDES)
    die2 = roll_die(NUM_SIDES)
    
    # Calculate the total
    total = die1 + die2
    
    # Print results
    print(f"Each die has {NUM_SIDES} sides.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of both dice: {total}")

# Ensure the script runs only when executed directly
if __name__ == '__main__':
    main()
