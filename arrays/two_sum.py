"""
Find two numbers that add up to a target value using a hash map.
"""

numbers = [2, 7, 11, 15]

def two_sum(numbers, target):

    seen = {}

    for index, number in enumerate(numbers):

        difference = target - number

        if difference in seen:
            return [seen[difference], index]
        
        seen[number] = index

    return []

print(two_sum(numbers, 9))