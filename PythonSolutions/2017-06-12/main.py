from collections import Counter


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def rank(self):
        return '234567890JQKA'.index(self.value)

    def __lt__(self, other):
        return self.rank() < other.rank()


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
        return (self.card_value in '234567890JQKA') or (self.card_value in '2345A')

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


hand1 = Hand([Card('6', 'D'), Card('4', 'C'), Card('4', 'D'), Card('4', 'D'), Card('J', 'D')])
hand1.print_hand()
hand2 = Hand([Card('9', 'D'), Card('5', 'C'), Card('5', 'D'), Card('5', 'D'), Card('0', 'D')])
hand2.print_hand()
print hand2 > hand1

