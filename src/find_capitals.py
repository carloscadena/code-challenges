"""Find the Capitals

#1 Best Practices Solution by deantwo & others

def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]
"""


def capitals(word):
    indexes = []
    print(len(word))
    for i in range(len(word)):
        if word[i].isupper():
            indexes.append(i)
    return indexes
