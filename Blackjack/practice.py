cards = Deck()
cards.shuffle_cards()
print(cards.cardslist)
print(len(cards.cardslist))

print("*****  Welcome to Cascais Casino  *****")
player_name = input("What is your name? ")
print("Good luck " + player_name + "\n")

player1 = Player()
player1.name = player_name
dealer1 = Dealer()

initial_deal(player1, dealer1, cards)

player1.print_hand()
print("Your score is: {}\n".format(player1.get_score()))
dealer1.print_first_hand()

dealer1.print_hand()
print("Your score is: {}\n".format(dealer1.get_score()))

print(len(cards.cardslist))

player1.hand = cards.get_cards(1, player1.hand)
player1.print_hand()
print("Your score is: {}\n".format(player1.get_score()))

print(len(cards.cardslist))