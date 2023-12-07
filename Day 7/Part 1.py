from collections import Counter

def get_numerical(card):
    if card.isdigit():
        return int(card)
    return {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}[card]

hands = []
with open('cards.txt', 'r') as f:
    for line in f.readlines():
        hand, bid = line.strip().split()
        bid = int(bid)
        hand = tuple(get_numerical(card) for card in hand)
        hands.append((hand, bid))

def get_strength(hand):
    trick_strength = tuple(sorted(Counter(hand).values(), reverse=True))
    return trick_strength, hand

hands.sort(key=lambda p: get_strength(p[0]))

print(sum(pair[1] * (i+1) for i, pair in enumerate(hands)))
