
from deck import Deck
from player import Player
from dealer import Dealer

# This is the move variable that will keep tracl of Stand or Hit
move = ""

# Function to Deal the initial cards to the Player and Dealer
def initial_deal(player, dealer, deck):
    player.hand = deck.get_cards(1, player.hand)
    dealer.hand = deck.get_cards(1, dealer.hand)
    player.hand = deck.get_cards(1, player.hand)
    dealer.hand = deck.get_cards(1, dealer.hand)

# Initialize the deck and shuffle the cards
cards = Deck()
cards.shuffle_cards()

# Prints the Welcome Message
print()
print("*****  Welcome to Cascais Casino  *****")
player_name = input("What is your name? ")
print("Good luck " + player_name + "\n")

# Initializes the Player and Dealer and names the Player
player1 = Player()
player1.name = player_name
dealer1 = Dealer()

# Calls the function to deal the initial cards to the Player and Dealer
initial_deal(player1, dealer1, cards)

# Prints out the Players hand and score
player1.print_hand()
print("Your score is: {}\n".format(player1.get_score()))

# Prints Dealers first hand with 1st card not shown
# Then checks if the Dealers wins BlackJack
dealer1.print_first_hand()
if dealer1.get_score() == 21:
    print("The House Wins!\n")
    dealer1.print_hand()

# Asks the Player if they want to Stand or Hit. Will exit out if Stand is chosen
# Checks if player goes over 21. If so then Busted message shown and breaks out of the function
while move != "s":    
    move = input("Do you want to Stand(s) or Hit(h)? ")
    
    if move == "h":
        player1.hand = cards.get_cards(1, player1.hand)
        player1.print_hand()
        print("Your score is: {}\n".format(player1.get_score()))
        if player1.get_score() > 21:
                print("You Busted!\n")
                break

dealer1.print_hand()
print("Dealer score is: {}\n".format(dealer1.get_score()))





