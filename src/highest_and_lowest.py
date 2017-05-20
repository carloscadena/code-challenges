"""Highest and Lowest

#1 Best Practices Solution by deantwo & others

def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
"""


def high_and_low(numbers):
    num_list = numbers.split(' ')
    results = [int(i) for i in num_list]
    return (str(max(results)) + ' ' + str(min(results)))
