"""Sort Deck of Cards

#1 Best Practices Solution by zebulan & others

def sort_cards(cards):
    return sorted(cards, key="A23456789TJQK".index)
"""


def sort_cards(cards):
    sorted_deck = []
    for x in cards:
        if x == 'A':
            sorted_deck.append('A')
    for x in cards:
        if x == '2':
            sorted_deck.append('2')
    for x in cards:
        if x == '3':
            sorted_deck.append('3')
    for x in cards:
        if x == '4':
            sorted_deck.append('4')
    for x in cards:
        if x == '5':
            sorted_deck.append('5')
    for x in cards:
        if x == '6':
            sorted_deck.append('6')
    for x in cards:
        if x == '7':
            sorted_deck.append('7')
    for x in cards:
        if x == '8':
            sorted_deck.append('8')
    for x in cards:
        if x == '9':
            sorted_deck.append('9')
    for x in cards:
        if x == 'T':
            sorted_deck.append('T')
    for x in cards:
        if x == 'J':
            sorted_deck.append('J')
    for x in cards:
        if x == 'Q':
            sorted_deck.append('Q')
    for x in cards:
        if x == 'K':
            sorted_deck.append('K')
    return sorted_deck
