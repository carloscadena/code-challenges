"""List Filtering

#1 Best Practices Solution by clawtros & others

def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]
"""


def filter_list(l):
    new_l = []
    for x in l:
        if isinstance(x, int):
            new_l.append(x)
    return new_l
