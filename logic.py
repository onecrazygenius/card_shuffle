# ./logic.py
# Logic for the game
# Handles importing a card class that is then used to create a deck of cards
# and then shuffle the deck
# The logic will also be able to draw a card from the deck and return it.

import random

from card import Card

class Deck:

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["s", "c", "d", "h"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))
    
    def shuffle(self):
        for i in range(len(self.cards)):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self, n=1):
        hand = []
        for i in range(n):
            hand.append(self.cards.pop())
        return hand
