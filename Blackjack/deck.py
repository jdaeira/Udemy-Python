
# This code will create a deck of cards
import random

class Deck():
    
    def __init__(self):
        self.cardslist = []
        self.suits = ("Hearts", "Diamonds", "Spades", "Clubs")
        self.faces = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", \
                      "Nine", "Ten", "Jack", "Queen", "King", "Ace")

    # This will shuffle the deck of cards
    def shuffle_cards(self):
        for suit in self.suits:
            for face in self.faces:
                self.cardslist.append((suit, face))
        random.shuffle(self.cardslist)
    
    # Get a particular amount of cards from the cardslist
    def get_cards(self, amount, hand):
        for x in range(amount):
            suit, face = self.cardslist[0]
            hand.append((suit, face))
            del self.cardslist[0]
        return hand






