def main():
    try:
        # Get the three side lengths of the triangle
        side1 = float(input("Enter the length of Side 1: "))
        side2 = float(input("Enter the length of Side 2: "))
        side3 = float(input("Enter the length of Side 3: "))

        # Ensure all sides are positive
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            print("Error: Side lengths must be positive numbers!")
            return

        # Check if the sides can form a valid triangle
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            print("Error: These sides do not form a valid triangle.")
            return

        # Calculate and print the perimeter
        perimeter = side1 + side2 + side3
        print(f"The perimeter of the triangle is: {perimeter:.2f}")

    except ValueError:
        print("Error: Please enter valid numbers!")

if __name__ == '__main__':
    main()
