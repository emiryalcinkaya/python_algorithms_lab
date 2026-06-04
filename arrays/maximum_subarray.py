"""
Find the maximum subarray sum using Kadane's Algorithm.
"""

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maximum_subarray(numbers):

    current_sum = numbers[0]
    max_sum = numbers[0]

    for number in numbers[1:]:

        current_sum = max(number, current_sum + number)
        max_sum = max(max_sum, current_sum)

    return max_sum

print(maximum_subarray(numbers))