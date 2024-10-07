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
    
    # remove last from stack
    
    # check if removed closing bracket 


if __name__ == "__main__":
    is_valid(brackets="()")
    is_valid("()[]{}")
    is_valid("(]")
    is_valid("([])")
