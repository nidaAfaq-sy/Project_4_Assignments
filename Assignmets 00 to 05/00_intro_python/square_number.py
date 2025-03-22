def main():
    try:
        num = float(input("Type a number to see its square: "))
        print(f"{num} squared is {num ** 2}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
