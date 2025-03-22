def main():
    print("Debug: main() function started")  # Debugging ke liye

    anton: int = 21  
    beth: int = 6 + anton  
    chen: int = 20 + beth  
    drew: int = chen + anton  
    ethan: int = chen  

    # Print out all of the ages!
    print(f"Anton is {anton} years old")
    print(f"Beth is {beth} years old")
    print(f"Chen is {chen} years old")
    print(f"Drew is {drew} years old")
    print(f"Ethan is {ethan} years old")

if __name__ == '__main__':
    print("Debug: Script is running")  # Debugging ke liye
    main()
