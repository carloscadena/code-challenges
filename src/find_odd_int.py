"""Find the odd int

#1 Best Practices Solution by cerealdinner & others

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
"""


def find_it(seq):
    for x in seq:
        if seq.count(x) % 2 == 1:
            return(x)
