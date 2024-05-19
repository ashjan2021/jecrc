# 3.	Write a Python function to find the maximum and minimum numbers in a given list of numbers without using in built functions.



lst = [10,20,30,50,8,40]

def max(lst):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            max = lst [i]
    return max

def min(lst):
    for i in range(len(lst)-1):
        if lst[i]<lst[i+1]:
            min = lst [i]
    return min


print(" max = ",max(lst),'\n',"min = ",min(lst))