# # 4.	Write a Python program to find the longest word in a given list of words. If there are multiple words with the same length,
# #  return the first one encountered word.

# lst = ['ashish','devansh','soumya','piyush','arman','ravi','kartik']
# def longest_word(lst):
#     longest = lst[0]
#     for word in lst:
#         if len(word) > len(longest):
#             longest = word
#     print(longest)
        
        
#         # print(" word = ",word,'\n',"length = ",length)

# longest_word(lst)


# if multiple words have same length

lst = ['ravi','ashish','piyush','arman','soumya','kartik']
def longest_word(lst):
    longest = lst[0]
    for word in lst:
        if len(word) > len(longest):
            longest = word
    print(longest)
        
        
        # print(" word = ",word,'\n',"length = ",length)

longest_word(lst)