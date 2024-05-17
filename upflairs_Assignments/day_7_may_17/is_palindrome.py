# Write a Python function called is_palindrome that takes a string s as input and returns True if s is a palindrome 
# (reads the same forwards and backwards), otherwise returns False.

s = input("Enter the string : ")

def is_palindrome(s):
    reverse = s[::-1]
    if reverse == s:
        (f'"{s}" is a palindrome')
        return True
    else:
        print(f'"{s}" is not a palindrome.')
        return False

def main():
    if is_palindrome(s):
        print(f'"{s}" is a palindrome')    
    else:
        print(f'"{s}" is not a palindrome.')

main()
        
