"""Sum of the nth term of Series

#1 Best Practices Solution by MMMAAANNN & others

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
"""


def series_sum(n):
    denom = 4
    answer = 1
    if n == 0:
        return '0.00'
    for value in range(1, n):
        answer += 1/(denom)
        denom += 3
    return '{0:.2f}'.format(answer)
