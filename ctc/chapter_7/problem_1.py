SUITS = ['S', 'C', 'A', 'D']
VALUES = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']


class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_value(self, ace_value=11):
        if self.value in ['J', 'Q', 'K']:
            return 10
        elif self.value == 'A':
            return ace_value
        else:
            return int(self.value)


class Deck(object):
    def __init__(self, cards=[]):
        self.cards = cards

    def shuffle(self):
        pass

    def deal_hand(self):
        pass

    def deal_card(self):
        pass


class Hand(object):
    def __init__(self, cards=[]):
        self.cards = cards

    def add_card(self, card):
        self.cards.append(card)

    def get_score(self):
        return sum([k.get_value() for k in self.cards])
