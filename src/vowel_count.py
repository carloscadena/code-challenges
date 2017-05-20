"""Vowel Count

#1 Best Practices Solution by javafreak & others

def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")
"""


def get_count(inputStr):
    num_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in inputStr:
        if letter in vowels:
            num_vowels += 1

    return num_vowels
