"""
----------------------------------------------------------------------------------------------------
QUESTION 4:
    Write an efficient method that tells us whether or not an input string brackets
    ("{", "}", "(", ")", "[", "]") opened and closed properly.
----------------------------------------------------------------------------------------------------

Basically, check if a statement with brackets is balanced.
The most classic way to do this is by using a stack -- in Python we can use either lists or a deque.
The idea is that we read from the input text, add it to the stack and, if we encounter a closing
symbol which closes the previous opening symbol, we pop it from the stack.
"""

from collections import deque


def check_brackets(text: str) -> bool:
    """Check if a statement with brackets is balanced."""
    stack = deque()
    valid_pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    # Sanity check for the input
    if not all(map(lambda x: x in valid_pairs or x in valid_pairs.values(), text)):
        raise ValueError(
            "ERROR! Text input contains characters other than types of brackets."
        )

    opening_symbols = valid_pairs.values()

    for symbol in text:
        if symbol in opening_symbols:
            stack.append(symbol)
        else:
            if stack and valid_pairs[symbol] == stack[-1]:
                stack.pop()
            else:
                stack.append(symbol)

    if len(stack) != 0:
        return False

    return True


if __name__ == "__main__":
    text = input("Input the brackets to be checked: ")
    print(f"Is the expression balanced? {check_brackets(text)}")
