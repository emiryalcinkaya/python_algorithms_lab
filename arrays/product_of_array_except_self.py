"""
Calculate the product of all elements except the current one.
"""

numbers = [1, 2, 3, 4]

def product_except_self(numbers):

    result = []

    for i in range(len(numbers)):

        product = 1

        for j in range(len(numbers)):

            if i != j:
                product *= numbers[j]

        result.append(product)

    return result

print(product_except_self(numbers))