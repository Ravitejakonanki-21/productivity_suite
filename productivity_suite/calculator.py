def calculator_menu():
    print("Calculator Tool")
    a = float(input("Enter number 1: "))
    op = input("Enter operator (+ - * /): ")
    b = float(input("Enter number 2: "))

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b if b != 0 else "Error: Division by zero")
