"""
Code kata for testing parens are opened and closed correctly.
Return 1 if the string is “open”
(there are open parens that are not closed)
Return 0 if the string is “balanced”
(there are an equal number of open and closed parentheses in the string)
Return -1 if the string is “broken”
(a closing parens has not been proceeded by one that opens)
"""


def parens(string):
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        if i == ')':
            try:
                stack.pop()
            except IndexError:
                return -1
    if len(stack) == 0:
        return 0
    else:
        return 1
