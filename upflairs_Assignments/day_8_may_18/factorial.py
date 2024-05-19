# 1.	Write a Python program to calculate the factorial of a non-negative integer entered by the user.

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def main():
    n = int(input("Enter the non negative integer : "))
    if n > 0:
        print(factorial(n))
    else:
        print("You can enter only positive integer !")
    
main()