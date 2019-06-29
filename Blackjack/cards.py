
# This code will create a deck of cards
import random

class Deck():
    
    def __init__(self):
        self.cardslist = []
        self.suits = ("Hearts", "Diamonds", "Spades", "Clubs")
        self.faces = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", \
         "Nine", "Ten", "Jack", "Queen", "King", "Ace")

    def shuffle_cards(self):
        for suit in self.suits:
            for face in self.faces:
                self.cardslist.append((suit, face))
        random.shuffle(self.cardslist)
    
    def get_cards(self):
        suit, face = self.cardslist[0]
        del self.cardslist[0]
        print(f"Your card is a {face} of {suit}")

cards = Deck()
cards.shuffle_cards()
print(cards.cardslist)
print(len(cards.cardslist))
print(cards.cardslist[0])

cards.get_cards()
print(cards.cardslist)
print(len(cards.cardslist))

cards.get_cards()
print(cards.cardslist)
print(len(cards.cardslist))

hand = []



