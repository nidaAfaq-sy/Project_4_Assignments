import math  # Import math module for square root calculation

def main():
    while True:
        try:
            # Get the two side lengths from the user and cast them to be numbers
            side_ab = float(input("Enter the length of side AB: "))
            side_ac = float(input("Enter the length of side AC: "))

            if side_ab <= 0 or side_ac <= 0:
                print("Lengths must be positive numbers. Try again.")
                continue

            # Calculate the hypotenuse using the Pythagorean theorem
            hypotenuse_bc = math.sqrt(side_ab**2 + side_ac**2)

            # Display the result
            print(f"The length of BC (the hypotenuse) is: {hypotenuse_bc:.2f}")
            break

        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Ensures the script runs only when executed directly
if __name__ == '__main__':
    main()
