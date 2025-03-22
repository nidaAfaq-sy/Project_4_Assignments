def main():
    # Get the year to check from the user
    year = int(input("Enter a year: "))

    # Check leap year conditions
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("It's a leap year!")
    else:
        print("It's not a leap year.")

# No need to edit beyond this point
if __name__ == "__main__":
    main()
