"""Shortest Word

#1 Best Practices Solution by MMMAAANNN & others

def find_short(s):
    return min(len(x) for x in s.split())
"""


def find_short(s):
    word_list = s.split(' ')
    return len(sorted(word_list, key=len)[0])
