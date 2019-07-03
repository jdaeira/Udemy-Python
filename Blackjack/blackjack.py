
from deck import Deck
from player import Player
from dealer import Dealer



cards = Deck()
cards.shuffle_cards()
print(cards.cardslist)
print(len(cards.cardslist))

player1 = Player()
dealer1 = Dealer()

player1.hand = cards.get_cards(1, player1.hand)
dealer1.hand = cards.get_cards(1, dealer1.hand)
player1.hand = cards.get_cards(1, player1.hand)
dealer1.hand = cards.get_cards(1, dealer1.hand)

player1.print_hand()
print("Your score is: {}".format(player1.get_score()))
dealer1.print_first_hand()

dealer1.print_hand()
print("Your score is: {}".format(dealer1.get_score()))

print(len(cards.cardslist))