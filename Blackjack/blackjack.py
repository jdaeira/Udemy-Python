
from deck import Deck
from player import Player
from dealer import Dealer

# This is the move variable that will keep tracl of Stand or Hit
move = ""
play = True 

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

# This is temporary till I figure out how to deal with the Aces
if player1.get_score() > 21:
    print("Player Busted!")
    exit()

# Prints Dealers first hand with 1st card not shown
# Checks if the Dealer and Player PUSH(tie)
# Checks if the Player wins Blackjack
# Then checks if the Dealers wins BlackJack
dealer1.print_first_hand()
if dealer1.get_score() == 21 and player1.get_score() == 21:
    print("PUSH")
    dealer1.print_hand()
elif player1.get_score() == 21:
    print("Blackjack! Player Wins!\n")
elif dealer1.get_score() == 21:
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
            print("Dealer Wins!\n")
            exit()    

# Will get a card card from the dealer till the score is 17 or more
dealer1.print_hand()
while dealer1.get_score() < 17:
    dealer1.hand = cards.get_cards(1, dealer1.hand)
    dealer1.print_hand()
    print("Dealer score is: {}\n".format(dealer1.get_score()))  

# Check to see if the Dealer busted
if dealer1.get_score() > 21:
    print("Dealer Busted\n")
# Checks to see if the Final result is a Tie
elif dealer1.get_score() <= 21 and dealer1.get_score() == player1.get_score():
    print("PUSH\n")
# Checks to see if the Dealer Wins the game
elif dealer1.get_score() <= 21 and dealer1.get_score() > player1.get_score():
    print("Dealer Wins!")
# Checks to see if the Player Wins the game
elif dealer1.get_score() <= 21 and dealer1.get_score() < player1.get_score():
    dealer1.print_hand()
    print(dealer1.get_score())
    print("Player Wins!")

#dealer1.print_hand()
#print("Dealer score is: {}\n".format(dealer1.get_score()))
