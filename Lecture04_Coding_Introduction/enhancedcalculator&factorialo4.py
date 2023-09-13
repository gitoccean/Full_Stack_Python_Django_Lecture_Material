
# Create functions according to arithmatic required
def add(x,y):         # Addition
    return x + y

def subtract(x,y):         # Subtraction
    return x - y

def multiply(x,y):        # Multiplication
    return x * y

def divide (x,y):          # Division
    if y != 0:
        return x / y
    else:
        return "cannot divide by Zero"


def factorial(x,y):                # factorial
    if x == 0 or y == 0 or x == 1 or y == 1:
        return 1
    else:
       return  x * factorial(x-1) , y * factorial(y-1)



# Heading
print("Welcome to the Enhance Calculator!")


    # user's name
user = str(input("Please enter your name: "))
yes = 'yes'
# While loop running from here
while yes == 'yes':
         num1 = int(input(f'{user}! Please enter the first number: '))
         num2 = int(input('Please enter the second number: '))


         # show off all operators, user can use for calculation
         print("Available Operations:")
         print("1. Addition (+)")
         print("2. Subtraction (-)")
         print("3. Multiplication (*)")
         print("4. Division (/)")
         print("5. Factorial(!)")


        # choose logic symbol by number
         operation = input("Please enter the operation (1/2/3/4/5): ")



        # code drive in case of number
         if operation == "1":
               result = add(num1,num2)
               operator = "+"
         elif operation == "2":
               result = subtract(num1,num2)
               operator = "-"
         elif operation == "3":
               result = multiply(num1,num2)
               operator = "*"
         elif operation == "4":
               result = divide(num1,num2)
               operator = "/"
         elif operation == "5":
               if num1 < 0 or num2 < 0:
                    print("Factorial is not defined for negative numbers.")
               else:
                    result = factorial(num1,num2)
                    operator = "!"
         else:
              result = "Invalid Operation"
              operator = ""


         # show of result of calculation
         print(f"Result: {num1} {operator} {num2} = {result}")




         # asking about another calculation
         boolean = str(input("Do you want to perform another calculation? (yes/no): "))


         # conditions about above statement
         if boolean != 'yes' :
              print("Thank you for using Enhanced Calculator. ")
              break
