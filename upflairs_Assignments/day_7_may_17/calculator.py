# Write a Python function called calculator that takes three arguments: num1 (float), num2 (float), and operation (string). 
# The function should perform the specified operation ('add', 'subtract', 'multiply', 'divide') on num1 and num2 and return the result

def calculator( num1 , num2 , operation ):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2  
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "ERROR ! Division by zero is not allowed"
    else:
        return "Invalid error"

      

def main():
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))
    operation = input("Enter the operation you want to perform : ")
    result = calculator( num1 , num2 , operation )
    print(result)

main()