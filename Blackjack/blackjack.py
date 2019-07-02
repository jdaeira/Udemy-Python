
from deck import Deck
from player import Player
from dealer import Dealer

cards = Deck()
cards.shuffle_cards()
print(cards.cardslist)
print(len(cards.cardslist))
print(cards.cardslist[0])

player1 = Player()
player1.hand = cards.get_cards(2, player1.hand)
print(player1.hand)

print("Your score is: {}".format(player1.get_score()))

player1.hand = cards.get_cards(1, player1.hand)
print(player1.hand)

print("Your score is: {}".format(player1.get_score()))

dealer1 = Dealer()

dealer1.hand = cards.get_cards(2, dealer1.hand)
print(dealer1.hand)

print("Your score is: {}".format(dealer1.get_score()))

dealer1.hand = cards.get_cards(1, dealer1.hand)
print(dealer1.hand)

print("Your score is: {}".format(dealer1.get_score()))

print(f"*  {player1.hand[0][1]}  of  {player1.hand[0][0]}  *")
