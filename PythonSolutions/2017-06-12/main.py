from collections import Counter
import numpy as np
import itertools

values = '234567890JQKA'
suits = 'CHSD'


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def rank(self):
        return values.index(self.value)

    def __eq__(self, other):
        if self.value == other.value and self.suit == other.suit:
            return True

        return False

    def __lt__(self, other):
        return self.rank() < other.rank()

    def __str__(self):
        return self.value + self.suit


class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.card_value = ''
        for c in self.cards:
            self.card_value += c.value

        self.tier = self.get_tier()
        self.sort_cards()

    def print_hand(self):
        for c in self.cards:
            print c.value + c.suit,

        print

    def is_flush(self):
        for i in range(len(self.cards) - 1):
            if self.cards[i].suit != self.cards[i+1].suit:
                return False

        return True

    def is_straight(self):
        return (self.card_value in values) or (self.card_value in '2345A')

    def is_four_of_a_kind(self):
        return max(Counter(self.card_value).values()) == 4

    def is_three_of_a_kind(self):
        cards = (Counter(self.card_value).values())
        cards.sort(reverse=True)
        return cards == [3, 1, 1]

    def is_full_house(self):
        cards = (Counter(self.card_value).values())
        cards.sort(reverse=True)
        return cards == [3, 2]

    def is_two_pairs(self):
        cards = (Counter(self.card_value).values())
        cards.sort(reverse=True)
        return cards == [2, 2, 1]

    def is_pair(self):
        cards = (Counter(self.card_value).values())
        cards.sort(reverse=True)
        return cards == [2, 1, 1, 1]

    def get_tier(self):
        if self.is_straight() and self.is_flush():
            return 9
        elif self.is_four_of_a_kind():
            return 8
        elif self.is_full_house():
            return 7
        elif self.is_flush():
            return 6
        elif self.is_straight():
            return 5
        elif self.is_three_of_a_kind():
            return 4
        elif self.is_two_pairs():
            return 3
        elif self.is_pair():
            return 2
        else:
            return 1

    def sort_cards(self):
        if self.tier in [9, 5]:
            self.cards.sort(key=Card.rank, reverse=True)
            if 'A' in self.card_value and '2' in self.card_value:
                self.cards = self.cards[1:] + [self.cards[0]]

        elif self.tier in [8, 7, 4, 2]:
            x_of_this = Counter(self.card_value).most_common(1)[0][0]
            tmp = [card for card in self.cards if card.value == x_of_this]
            self.cards = tmp + sorted([card for card in self.cards if card.value != x_of_this],
                                      key=Card.rank, reverse=True)

        elif self.tier in [6, 1]:
            self.cards.sort(key=Card.rank, reverse=True)

        elif self.tier == 3:
            pairs = [v for v, _ in Counter(self.card_value).most_common(2)]
            tmp = sorted([card for card in self.cards if card.value in pairs], key=Card.rank, reverse=True)
            self.cards = tmp + [card for card in self.cards if card.value not in pairs]

    def __lt__(self, other):
        if self.tier < other.tier:
            return True
        elif self.tier == other.tier:
            for i in range(5):
                if self.card_value[i] < other.card_value[i]:
                    return True
                elif self.card_value[i] > other.card_value[i]:
                    return False

        else:
            return False
        return False

    def __eq__(self, other):
        if self.tier == other.tier:
            for card_s, card_o in zip(self.cards, other.cards):
                if card_s.rank() != card_o.rank():
                    return False
            return True
        return False

    def __str__(self):
        tmp_string = ''
        for c in self.cards:
            tmp_string = tmp_string + c.value + c.suit

        return tmp_string


def get_card_from_string(give_card_string):
    return Card(give_card_string[0], give_card_string[1])


def build_deck():
    tmp_full_deck = []
    for v in values:
        for s in suits:
            tmp_full_deck.append(Card(v, s))

    return tmp_full_deck


def all_subsets(ss):
    return itertools.chain(*map(lambda a: itertools.combinations(ss, a), range(0, len(ss)+1)))


filename = 'input1.txt'
with open(filename) as f:
    content = f.readlines()

content = [x.strip() for x in content]
player_num = len(content) - 1

flop_string = content[0]
flop_cards = [get_card_from_string(x) for x in [flop_string[i:i+2] for i in range(0, len(flop_string), 2)]]

player_cards = []
for i in range(1, len(content)):
    card_string = content[i]
    tmp_cards = [get_card_from_string(x) for x in [card_string[i:i+2] for i in range(0, len(card_string), 2)]]
    player_cards.append(tmp_cards)

# Build the full deck
deck = build_deck()
# Remove the ones given to players and the flop
for p in player_cards:
    for c in p:
        if c in deck:
            deck.remove(c)
        else:
            print 'Error in given cards'
            exit(1)

for c in flop_cards:
    if c in deck:
        deck.remove(c)
    else:
        print 'Error in given cards'
        exit(1)

player_scores = np.zeros(player_num)
for turn_card in deck:
    new_deck = [x for x in deck if x != turn_card]
    for river_card in new_deck:
        show_down_hands = []
        for p in player_cards:
            seven_cards = []
            for c in p:
                seven_cards.append(c)

            for c in flop_cards:
                seven_cards.append(c)

            seven_cards.append(turn_card)
            seven_cards.append(river_card)

            player_hands_combinations = itertools.combinations(seven_cards, 5)
            player_hands = []
            for hand_tuple in player_hands_combinations:
                player_hands.append(Hand(list(hand_tuple)))

            show_down_hands.append(max(player_hands))

        winning_player_index = np.argmax(show_down_hands)
        player_scores[winning_player_index] += 1

print player_scores
player_scores /= len(deck) * (len(deck) - 1)
print player_scores
