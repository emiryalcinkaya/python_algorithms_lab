"""
Sort a list using the insertion sort algorithm.
"""

def insertion_sort(numbers):

    for i in range(1, len(numbers)):

        current_number = numbers[i]
        j = i - 1

        while  j >= 0 and numbers[j] > current_number:

            numbers[j + 1] = numbers[j]
            j -= 1
            
        numbers[j + 1] = current_number
    
    return numbers

numbers = [64, 25, 12, 22, 11]

print(insertion_sort(numbers))