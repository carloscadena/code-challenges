"""String Pyramid

#1 Best Practices Solution by Blind4Basics

def watch_pyramid_from_the_side(characters):
    if not characters : return characters
    baseLen = len(characters)*2-1
    return '\n'.join( ' '*(i) + characters[i]*(baseLen-2*i) + ' '*(i) for i in range(len(characters)-1,-1,-1) )


def watch_pyramid_from_above(characters):
    if not characters : return characters
    baseLen = len(characters)*2-1
    return '\n'.join( characters[0:min(i,baseLen-1-i)] + characters[min(i,baseLen-1-i)]*(baseLen-2*min(i,baseLen-1-i)) + characters[0:min(i,baseLen-1-i)][::-1] for i in range(baseLen) )


def count_visible_characters_of_the_pyramid(characters):
    return -1 if not characters else (len(characters)*2-1)**2


def count_all_characters_of_the_pyramid(characters):
    return -1 if not characters else sum( (2*i+1)**2 for i in range(len(characters)) )
"""


def watch_pyramid_from_the_side(characters):
    if characters:
        if '\n' in characters:
            characters = characters.replace("\n", "")
        side = ''
        base = 1
        spaces = len(characters) - 1
        for i, item in enumerate(characters[::-1]):
            side += (' ' * (spaces - i)) + item * base + (' ' * (spaces - i)) + '\n'
            base += 2
        return side[:-1]
    else:
        return characters


def watch_pyramid_from_above(characters):
    if characters:
        if '\n' in characters:
            characters = characters.replace("\n", "")
        north = ''
        south = ''
        count = (len(characters) * 2) - 1
        before = ''
        if len(characters) == 1:
            return characters
        for i, char in enumerate(characters):
            row = before + (char * count) + before[::-1] + '\n'
            north += row
            if i != len(characters) - 1:
                south = row + south
            before += char
            count -= 2
        return north + south[:-1]
    else:
        return characters


def count_visible_characters_of_the_pyramid(characters):
    if characters:
        if '\n' in characters:
            characters = characters.replace("\n", "")
        return ((len(characters) * 2) - 1) ** 2
    else:
        return -1


def count_all_characters_of_the_pyramid(characters):
    if characters:
        if '\n' in characters:
            characters = characters.replace("\n", "")
        base = (len(characters) * 2) - 1
        total = 0
        for char in range(len(characters)):
            total += base ** 2
            base -= 2
        return total
    else:
        return -1
