"""Prefill an Array

#1 Best Practices Solution by HEXecutive

def prefill(n=0,v=None):
    try:
        return [v] * int(n)
    except:
        raise TypeError(str(n) + ' is invalid')
"""


def prefill(n, v=None):
    answer = []
    try:
        n = int(n)
    except (ValueError, TypeError):
        raise TypeError(str(n) + ' is invalid')
    if n == 0:
        return answer
    if not v:
        return [v] * int(n)
    answer.append(v)
    return answer * int(n)
