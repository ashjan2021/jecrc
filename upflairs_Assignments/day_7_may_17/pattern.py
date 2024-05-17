# 4.	Write a Python function called right_triangle_pattern that takes an integer n as input and prints a right triangle pattern of n rows. Each row should contain i asterisks (*), where i is the row number.
# Example: For n = 5, the pattern should be:

# *
# * *
# * * *
# * * * *
# * * * * *

def right_triangle_pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print('*',end ="")
        print('\n')


def main():
    n = int(input("Enter the integer n : "))
    pattern = right_triangle_pattern(n)

main()