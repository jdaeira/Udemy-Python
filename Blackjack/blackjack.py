
from deck import Deck
from player import Player
from dealer import Dealer

def initial_deal(player, dealer, deck):
    player.hand = deck.get_cards(1, player.hand)
    dealer.hand = deck.get_cards(1, dealer.hand)
    player.hand = deck.get_cards(1, player.hand)
    dealer.hand = deck.get_cards(1, dealer.hand)


cards = Deck()
cards.shuffle_cards()
print(cards.cardslist)
print(len(cards.cardslist))

player1 = Player()
dealer1 = Dealer()

initial_deal(player1, dealer1, cards)

player1.print_hand()
print("Your score is: {}".format(player1.get_score()))
dealer1.print_first_hand()

dealer1.print_hand()
print("Your score is: {}".format(dealer1.get_score()))

print(len(cards.cardslist))

player1.hand = cards.get_cards(1, player1.hand)
player1.print_hand()
print("Your score is: {}".format(player1.get_score()))