"""
Search for an element in a sorted list using binary search.
"""

def binary_search(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left <= right:

        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        elif numbers[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1


numbers = [2, 5, 7, 9, 11, 17, 222]

print(binary_search(numbers, 11))
print(binary_search(numbers, 12))