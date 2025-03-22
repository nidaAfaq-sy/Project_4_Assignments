"""
Feet to Inches Converter
"""

INCHES_IN_FOOT: int = 12  # 1 foot = 12 inches

def main():
    try:
        feet: float = float(input("Enter the number of feet: "))  # Input as float
        inches: float = feet * INCHES_IN_FOOT  # Conversion
        print(f"{feet} feet is equal to {inches:.2f} inches.")  # Formatted output
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

if __name__ == '__main__':
    main()
