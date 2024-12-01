import Calc

while True:
    command = input("Enter a command ('add', 'sub', 'mult', 'div', or 'stop' to exit): ")
    
    if command == "stop":
        print("Exiting the calculator. Goodbye!")
        break

    if command not in ["add", "sub", "mult", "div"]:
        print("Invalid command. Please try again.")
        continue

    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    if command == "add":
        result = Calc.add(num1, num2)
    elif command == "sub":
        result = Calc.sub(num1, num2)
    elif command == "mult":
        result = Calc.mult(num1, num2)
    elif command == "div":
        result = Calc.div(num1, num2)

    print(f"The result of {command} operation is: {result}")

    cont = input("Would you like to perform another operation? (yes or stop): ")
    if cont == "stop":
        print("Exiting the calculator. Goodbye!")
        break
