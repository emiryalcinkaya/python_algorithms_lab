"""
Check whether parentheses are valid using a stack.
"""

def is_valid_parentheses(text):

    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for character in text:

        if character in "([{":
            stack.append(character)

        elif character in ")]}":

            if not stack:
                return False
            
            last_open = stack.pop()

            if last_open != pairs[character]:
                return False
            
    return len(stack) == 0

print(is_valid_parentheses("()[]{}"))
print(is_valid_parentheses("([{}])"))
print(is_valid_parentheses("([)]"))
