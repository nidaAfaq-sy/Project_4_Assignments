def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_price = 0
    for fruit_name, price in fruits.items():
        while True:
            try:
                amount_bought = int(input(f"Enter quantity for {fruit_name}: "))
                if amount_bought < 0:
                    print("Quantity cannot be negative. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a whole number.")

        total_price += price * amount_bought

    print("\nYour total cost is: $", round(total_price, 2))


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
