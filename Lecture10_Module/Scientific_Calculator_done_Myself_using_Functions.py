def addition(a,b):
    return (a+b)


def subtraction(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def division(a,b):
    if b == 0:
        print("Sorry! cannot divide by Zero.")
    else:
        return(a/b)
import math
from calculator_bonus import *

def perform_addition():
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = addition(num1, num2)
    print(f"Answer: {num1} + {num2} = {result}")

def perform_subtraction():
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = subtraction(num1, num2)
    print(f"Answer: {num1} - {num2} = {result}")

def perform_multiply():
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = multiply(num1, num2)
    print(f"Answer: {num1} * {num2} = {result}")

def perform_division():
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    if num2 != 0:
        result = division(num1, num2)
        print(f"Answer: {num1} / {num2} = {result}")
    else:
        print("ValueError: Division by zero")

def perform_sin():
    num3 = int(input("Enter the number: "))
    result = math.sin(math.radians(num3))
    print(f"Answer: sin({num3}) = {result}")

def perform_cos():
    num4 = int(input("Enter the number: "))
    result = math.cos(math.radians(num4))
    print(f"Answer: cos({num4}) = {result}")

def perform_tan():
    num5 = int(input("Enter the number: "))
    result = math.tan(math.radians(num5))
    print(f"Answer: tan({num5}) = {result}")

def perform_exponent():
    num5 = int(input("Enter the number: "))
    result = math.exp(num5)
    print(f" Power of {num5} = {result}")

def perform_factorial():
    num5 = int(input("Enter the number: "))
    result = math.factorial(num5)
    print(f"Answer: {num5}! = {result}")

def perform_log():
    num5 = int(input("Enter the number: "))
    result = math.log(num5)
    print(f"Answer: log{num5} = {result}")

def perform_natural_log():
    num5 = int(input("Enter the number: "))
    e = float(input("Enter the base: "))
    result = math.log(num5, e)
    print(f"Answer: ln{num5} = {result}")

def perform_power():
    num6 = int(input("Enter the number: "))
    num7 = int(input("Enter the exponent digit: "))
    result = math.pow(num6, num7)
    print(f"Answer: {num6}^{num7} = {result}")

def perform_module():
    num1 = int(input("Enter the dividend number: "))
    num2 = int(input("Enter the divisor number: "))
    if num2 != 0:
        result = float(math.fmod(num1, num2))
        print(f"Answer: {num1} mod {num2} = {result}")
    else:
        print("ValueError: Division by zero")

def perform_square_root():
    num5 = int(input("Enter the number: "))
    if num5 >= 0:
        result = math.sqrt(num5)
        print(f"Answer: square root of {num5} = {result}")
    else:
        print("ValueError: Cannot calculate square root of a negative number")

while True:
    print("*** Basic Calculator *")
    print("***** Scientific Calculator ***")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiply")
    print("4: Division")
    print("5: Sin")
    print("6: Cos")
    print("7: Tan")
    print("8: Exponent")
    print("9: Factorial")
    print("10: Log")
    print("11: Natural Log (ln)")
    print("12: Power")
    print("13: Module")
    print("14: Square Root")

    operation = int(input("What operation do you want to perform: "))

    if operation == 1:
        perform_addition()
    elif operation == 2:
        perform_subtraction()
    elif operation == 3:
        perform_multiply()
    elif operation == 4:
        perform_division()
    elif operation == 5:
        perform_sin()
    elif operation == 6:
        perform_cos()
    elif operation == 7:
        perform_tan()
    elif operation == 8:
        perform_exponent()
    elif operation == 9:
        perform_factorial()
    elif operation == 10:
        perform_log()
    elif operation == 11:
        perform_natural_log()
    elif operation == 12:
        perform_power()
    elif operation == 13:
        perform_module()
    elif operation == 14:
        perform_square_root()
    else:
        print("Invalid choice! Please choose a valid operation.")      
