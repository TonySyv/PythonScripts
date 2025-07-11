# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == '+':
        print(f"Result: {add(num1, num2)}")
    elif operation == '-':
        print(f"Result: {subtract(num1, num2)}")
    elif operation == '*':
        print(f"Result: {multiply(num1, num2)}")
    elif operation == '/':
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid operation.")
