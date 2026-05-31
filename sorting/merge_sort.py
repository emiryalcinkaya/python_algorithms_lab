"""
Sort a list using the merge sort algorithm.
"""

def merge_sort(numbers):

    if len(numbers) <= 1:
        return numbers
    
    middle = len(numbers) // 2

    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    return merge(left, right)

def merge(left, right):
    
    result = []

    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):

        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1

        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

numbers = [64, 25, 12, 22, 11]

print(merge_sort(numbers))