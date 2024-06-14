
file = open('description.txt','r')
print(file.read())
file.close()

# defining  functions to perform an arithmatic operation between two numbers
def add(x,y):
    c = x+y
    return c

def sub(x,y):
    c = x-y
    return c

def multiply(x,y):
    c = x*y
    return c

def divide(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
        #to handle the error
    c = x/y
    return c

def modulation(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
        #to handle the error
    c = x%y
    return c

import re

#to handle errors we have used try and except function.
while True:
    # Prompt the user to enter an expression in the format "number1 operator number2"
    user_input = input("Enter any mathematical expression (e.g., 1+3): \n")

    # Use a regular expression to find the numbers and the operator
    match = re.match(r"(\d+)\s*([+\-*/ %])\s*(\d+)", user_input)

    if match:
        num1 = int(match.group(1))
        operator = match.group(2)
        num2 = int(match.group(3))
        
        try:
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = sub(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            elif operator == '%':
                result = modulation(num1, num2)

            print(f"The result of {num1} {operator} {num2} is: {result}")
            break  # Exit the loop if the operation is successful
        except ValueError as e:
            print(e)
    else:
        print("Invalid input. Please enter an expression in the format 'number1 operator number2'.")



