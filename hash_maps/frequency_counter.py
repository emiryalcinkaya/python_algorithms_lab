"""
Count the frequency of each element using a hash map.
"""

def count_frequency(numbers):

    frequency = {}

    for number in numbers:

        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    return frequency


numbers = [1, 2, 2, 3, 3, 3, 4]

print(count_frequency(numbers))