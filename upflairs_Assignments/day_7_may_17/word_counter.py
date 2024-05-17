# Write a python function called wordCounter that takes a string “S” as an input, and return the count of each character in word or in “S”.
# e.g pass S = “uplfairs pvt ltd”
# u -> 1
# p -> 2
# l ->  2
# and so on .


def word_counter(S):
    unique_characters = set(S)
    for char in unique_characters:
        count = 0
        for c in S:
            if c == char:
                count += 1
        print(f'{char} -> {count}')
                    
def main():
    S = input("Enter the word : ")
    word_counter(S)

main()