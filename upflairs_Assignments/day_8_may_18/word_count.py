# 2.	Write a Python program to read a text file line by line and display the number of words in each line. Create a dome text file by it yourself for this assignment.

# it is a program to count the words in a single line string.
def word_count(s):
    count = 1
    for item in s:
        if item == ' ':
            count+=1
    return count+1

def main():
    s = input("enter the string : ")
    print(word_count(s)) 

main()

