# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"
# Output: true

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    # The stack to keep track of opening brackets.
    stack = []

    # Hash map for keeping track of mappings. This keeps the code very clean.
    # Also makes adding more types of parenthesis easier
    mapping = {")": "(", "}": "{", "]": "["}

    # For every bracket in the expression.
    for char in s:

        # If the character is an closing bracket
        if char in mapping:

            # Pop the topmost element from the stack, if it is non empty
            # Otherwise assign a dummy value of '#' to the top_element variable
            top_element = stack.pop() if stack else '#'

            # The mapping for the opening bracket in our hash and the top
            # element of the stack don't match, return False
            if mapping[char] != top_element:
                return False
        else:
            # We have an opening bracket, simply push it onto the stack.
            stack.append(char)

    # In the end, if the stack is empty, then we have a valid expression.
    # The stack won't be empty for cases like ((()
    return not stack

print(isValid("(([]{}))"))
#1st iteration stack = ["("" ]
#2 iteration   stack = ["(,( "]
#3 iteration   stack = ["(,(,[ "]
#4 iteration   stack = []
#5 iteration
#6 iteration
#7 iteration
#8 iteration



def isValid(s):
    #create a stack to keep track of the opening brackets
    #create a hashmap to check if the character in the string matches with the element in the hashmap
    # itereate through the string
        #if the character in string is in the map
            #create top element variable = stack.pop remove the upmost element from the stack. if the stack is empty assign a dummy element of '#'
            #if the top element is not equal to the mapping character
            #return false

        #else
            #append the element to the stack using stack.append(character)

    stack = []

    mapping = 
