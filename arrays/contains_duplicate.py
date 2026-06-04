"""
Check whether a list contains duplicate values.
"""

numbers = [1, 2, 3, 4, 2]

def contains_duplicate(numbers):

    seen = set()

    for number in numbers:

        if number in seen:
            return True
        
        seen.add(number)

    return False

print(contains_duplicate(numbers))