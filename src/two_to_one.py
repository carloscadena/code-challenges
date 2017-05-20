"""Two to One

#1 Best Practices Solution by cerealdinner & others

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))
"""


def longest(s1, s2):
    combo_string = set(s1 + s2)
    return ''.join(sorted(combo_string))
