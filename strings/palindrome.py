"""
Check whether a word is a palindrome.
"""

def is_palindrome(word):

    reversed_word = word[::-1]

    if word == reversed_word:
        return True
    
    return False

word = input("Enter a word: ")

print(is_palindrome(word))