"""
Sort a list using the quick sort algorithm.
"""

def quick_sort(numbers): 

    if len(numbers) <= 1:
        return numbers
    
    pivot = numbers[0]

    smaller = []
    greater = []

    for number in numbers[1:]:

        if number <= pivot:
            smaller.append(number)

        else:
            greater.append(number)

    return quick_sort(smaller) + [pivot] + quick_sort(greater)

numbers = [64, 25, 12, 22, 11]

print(quick_sort(numbers))
