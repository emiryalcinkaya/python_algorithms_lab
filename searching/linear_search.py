"""
Search for an element in a list using linear search.
"""

def linear_search(numbers, target):

    for index in range(len(numbers)):

        if numbers[index] == target:
            return index

    return -1


numbers = [10, 25, 30, 45, 50]

print(linear_search(numbers, 45))
print(linear_search(numbers, 99))