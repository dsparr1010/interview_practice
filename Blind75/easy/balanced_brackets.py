"""
    
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    

    Example 1:

    Input: s = "()"

    Output: true

    Example 2:

    Input: s = "()[]{}"

    Output: true

    Example 3:

    Input: s = "(]"

    Output: false

    Example 4:

    Input: s = "([])"

    Output: true

"""


def is_valid(brackets: str) -> bool:

    # Utilize a dict to map closing bracket (key) to opening brackets (value)
    valid_parens = {"}": "{", "]": "[", ")": "("}
    opening_brackets_list = []
    # "(())"
    # []

    # bad to hardcode for specific case (risky)
    # if brackets[0] in valid_parens.keys():
    #   return False

    for elem in brackets:
        # IF OPEN PARENTHESIS, ADD TO NEW LIST
        if elem in valid_parens.values():
            opening_brackets_list.append(elem)
        else:
            if len(opening_brackets_list) == 0:
                return False

            if valid_parens[elem] == opening_brackets_list[-1]:
                opening_brackets_list.pop()

    return len(opening_brackets_list) == 0


if __name__ == "__main__":
    assert is_valid(brackets="()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([])") is True
    assert is_valid(")") is False
