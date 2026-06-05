"""
Find the missing number in a sequence from 1 to n.
"""

numbers = [1, 2, 3, 5]

def find_missing_number(numbers):

    n = len(numbers) + 1

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)

    return expected_sum - actual_sum

print(find_missing_number(numbers))