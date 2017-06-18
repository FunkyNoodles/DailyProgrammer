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


class Hand(object):
    def __init__(self, cards):
        assert len(cards) == 5

        self.cards = cards
        self.name = None
        self.tier = None
        self.get_type()
        self.sort_cards()

    def get_suits(self):
        return [card.suit for card in self.cards]

    def get_values(self):
        return [card.value for card in self.cards]

    def get_type(self):
        if len(set(self.get_suits())) == 1 and self.have_consecs():
            self.name = "Straight Flush"
            self.tier = 9
        elif max(Counter(self.get_values()).values()) == 4:
            self.name = "Four of a Kind"
            self.tier = 8
        elif set(Counter(self.get_values()).values()) == {3, 2}:
            self.name = "Full House"
            self.tier = 7
        elif len(set(self.get_suits())) == 1:
            self.name = "Flush"
            self.tier = 6
        elif self.have_consecs():
            self.name = "Straight"
            self.tier = 5
        elif set(Counter(self.get_values()).values()) == {3, 1}:
            self.name = "Three of a Kind"
            self.tier = 4
        elif list(Counter(self.get_values()).values()).count(2) == 2:
            self.name = "Two Pairs"
            self.tier = 3
        elif len(set(self.get_values())) == 4:
            self.name = "Pair"
            self.tier = 2
        else:
            self.name = "Highest Card"
            self.tier = 1

    def sort_cards(self):
        if self.name in ["Straight Flush", "Straight"]:
            self.cards.sort(key=Card.rank, reverse=True)
            if 'A' in self.get_values() and '2' in self.get_values():
                self.cards = self.cards[1:] + [self.cards[0]]

        elif self.name in ["Four of a Kind", "Full House", "Three of a Kind", "Pair"]:
            x_of_this = Counter(self.get_values()).most_common(1)[0][0]
            tmp = [card for card in self.cards if card.value == x_of_this]
            self.cards = tmp + sorted([card for card in self.cards if card.value != x_of_this],
                                      key=Card.rank, reverse=True)

        elif self.name in ["Flush", "Highest Card"]:
            self.cards.sort(key=Card.rank, reverse=True)

        elif self.name == "Two Pairs":
            pairs = [v for v, _ in Counter(self.get_values()).most_common(2)]
            tmp = sorted([card for card in self.cards if card.value in pairs], key=Card.rank, reverse=True)
            self.cards = tmp + [card for card in self.cards if card.value not in pairs]

    def have_consecs(self):
        value_list = "A234567890JQKA"
        possibles = []
        for i in range(1+len(value_list)-5):
            possibles.append(value_list[i:i+5])

        sorted_values = sorted(self.get_values(), key=lambda x: "234567890JQKA".index(x))
        if 'A' in self.get_values() and '2' in self.get_values():
            sorted_values = [sorted_values[-1]] + sorted_values[:-1]
        return ''.join(sorted_values) in possibles

    def __eq__(self, other):
        if self.tier == other.tier:
            for card_s, card_o in zip(self.cards, other.cards):
                if card_s.rank() != card_o.rank():
                    return False
            return True
        return False

    def __lt__(self, other):
        if self.tier < other.tier:
            return True
        elif self.tier == other.tier:
            for card_s, card_o in zip(self.cards, other.cards):
                if card_s.rank() < card_o.rank():
                    return True
                elif card_s.rank() > card_o.rank():
                    return False
        return False


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

            best_hand = max(player_hands)
            show_down_hands.append(best_hand)

        winning_player_index = np.argmax(show_down_hands)
        # if any([show_down_hands[x] == show_down_hands[winning_player_index] for x, y in enumerate(show_down_hands) if x != winning_player_index]):
        #     print 'tie'
        # else:
        player_scores[winning_player_index] += 1

print player_scores
player_scores /= len(deck) * (len(deck) - 1)
print player_scores
