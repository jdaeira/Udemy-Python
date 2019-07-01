
from deck import Deck
from player import Player

cards = Deck()
cards.shuffle_cards()
print(cards.cardslist)
print(len(cards.cardslist))
print(cards.cardslist[0])

# cards.get_cards()
# print(cards.cardslist)
# print(len(cards.cardslist))

# cards.get_cards()
# print(cards.cardslist)
# print(len(cards.cardslist))

# player_hand = []
# player_hand = cards.get_cards(5, player_hand)
# print(player_hand)


# player_hand = cards.get_cards(1, player_hand)
# print(player_hand)



player1 = Player()
player1.hand = cards.get_cards(2, player1.hand)
print(player1.hand)

player1.hand = cards.get_cards(1, player1.hand)
print(player1.hand)

print(player1.add_score(5))

print(player1.add_score(10))