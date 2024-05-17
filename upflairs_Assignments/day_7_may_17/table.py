# Write a Python function called multiplication_table that takes an integer n as input and prints the multiplication table of n up to 10.

def multiplication(n):
    for i in range(1,11):
        result = n * i
        print(f'{n} x {i} = {result}')

def main():
    n = int(input("Enter the integer n : "))
    multiplication(n)

main()