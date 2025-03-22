def main():
  try:
    num1 =(input("Enter The First Number"))
    num1 = int(num1)

    num2 =(input("Enter The Second Number"))
    num2 = int(num2)

    total = num1 + num2
    print(f"{num1} + {num2} = {total}")
  except ValueError:
    print("Invalid Input! Please Enter a Number only.")  
main()    