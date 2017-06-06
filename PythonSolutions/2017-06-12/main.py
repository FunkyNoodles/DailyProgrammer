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
        self.sort_cards()
        card_value = ''
        for c in self.cards:
            card_value += c.value

    def sort_cards(self):
        self.cards.sort()

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

    def __lt__(self, other):

        return False


hand = Hand([Card('A', 'D'), Card('3', 'C'), Card('2', 'D'), Card('5', 'D'), Card('4', 'D')])
hand.print_hand()
print hand.is_straight()

