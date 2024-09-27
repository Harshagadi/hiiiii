# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Function to perform exponentiation
def exponentiate(x, y):
    return x ** y

# Function to perform modulus
def modulus(x, y):
    if y == 0:
        return "Error: Modulus by zero"
    return x % y

# Function to perform floor division
def floor_divide(x, y):
    if y == 0:
        return "Error: Floor division by zero"
    return x // y

# Main calculator loop
while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'exponentiate' for exponentiation")
    print("Enter 'modulus' for modulus")
    print("Enter 'floor_divide' for floor division")
    print("Enter 'quit' to end the program")
    
    user_input = input(": ")
    
    if user_input == "quit":
        break
    
    if user_input in ("add", "subtract", "multiply", "divide", "exponentiate", "modulus", "floor_divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if user_input == "add":
            print("Result:", add(num1, num2))
        elif user_input == "subtract":
            print("Result:", subtract(num1, num2))
        elif user_input == "multiply":
            print("Result:", multiply(num1, num2))
        elif user_input == "divide":
            print("Result:", divide(num1, num2))
        elif user_input == "exponentiate":
            print("Result:", exponentiate(num1, num2))
        elif user_input == "modulus":
            print("Result:", modulus(num1, num2))
        elif user_input == "floor_divide":
            print("Result:", floor_divide(num1, num2))
    else:
        print("Invalid input")
