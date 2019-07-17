
from deck import Deck
from player import Player
from dealer import Dealer

# Function to Deal the initial cards to the Player and Dealer
def initial_deal(player, dealer, card):
    player.hand = card.get_cards(1, player.hand)
    dealer.hand = card.get_cards(1, dealer.hand)
    player.hand = card.get_cards(1, player.hand)
    dealer.hand = card.get_cards(1, dealer.hand)

# Function that check if a player want to continue playing
def play_again():
    print()
    answer = input("Do you want to play again y/n? ")
    if answer == "y":
        player1.hand = []
        dealer1.hand = []
        play_blackjack()
    else:
        print()
        print("Thank you for playing!")
        check_winnings = player1.money - player1.initial_bet
        if player1.money > player1.initial_bet:
            print(f"Congratulations! You won ${check_winnings}!")
        else:
            print(f"You lost ${abs(check_winnings)}. Better luck next time.\n")
        exit()

# Function that Starts or continues the game
def play_blackjack():
    move = ""

    # Initialize the deck and shuffle the cards
    cards = Deck()
    cards.shuffle_cards()

    # Ask how much to bet in the game
    print(f"You have ${player1.money} to bet!\n")
    bet = input("How much is your bet? ")
    player1.bet = int(bet)


    # Calls the function to deal the initial cards to the Player and Dealer
    initial_deal(player1, dealer1, cards)

    # Prints out the Players hand and score
    player1.print_hand()
    print("Your score is: {}\n".format(player1.get_score()))

    # This is temporary till I figure out how to deal with the Aces
    if player1.get_score() > 21:
        print("Player Busted!")
        play_again()

    # Prints Dealers first hand with 1st card not shown
    # Checks if the Dealer and Player PUSH(tie)
    # Checks if the Player wins Blackjack
    # Then checks if the Dealers wins BlackJack
    dealer1.print_first_hand()
    if dealer1.get_score() == 21 and player1.get_score() == 21:
        print("PUSH")
        dealer1.print_hand()
        play_again()
    elif player1.get_score() == 21:
        dealer1.print_hand()
        print("Dealer score is: {}\n".format(dealer1.get_score())) 
        print("Blackjack! Player Wins!\n")
        player1.win_bet()
        play_again()
    elif dealer1.get_score() == 21:
        dealer1.print_hand()
        print("The House Wins!\n")
        player1.lost_bet()
        play_again()
        
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
                dealer1.print_hand()
                print("Dealer Wins!\n")
                player1.lost_bet()
                play_again()   
    

    # Will get a card card from the dealer till the score is 17 or more
    dealer1.print_hand()
    while dealer1.get_score() < 17:
        dealer1.hand = cards.get_cards(1, dealer1.hand)
        dealer1.print_hand()
        #print("Dealer score is: {}\n".format(dealer1.get_score()))  

    # Check to see if the Dealer busted
    if dealer1.get_score() > 21:
        print("Dealer score is: {}\n".format(dealer1.get_score())) 
        print("Dealer Busted\n")
        player1.win_bet()
        play_again()
    # Checks to see if the Final result is a Tie
    elif dealer1.get_score() <= 21 and dealer1.get_score() == player1.get_score():
        print("Dealer score is: {}\n".format(dealer1.get_score())) 
        print("PUSH\n")
        play_again()
    # Checks to see if the Dealer Wins the game
    elif dealer1.get_score() <= 21 and dealer1.get_score() > player1.get_score():
        print("Dealer score is: {}\n".format(dealer1.get_score())) 
        print("Dealer Wins!")
        player1.lost_bet()
        play_again()
    # Checks to see if the Player Wins the game
    elif dealer1.get_score() <= 21 and dealer1.get_score() < player1.get_score():
        print("Dealer score is: {}\n".format(dealer1.get_score())) 
        print("Player Wins!")
        player1.win_bet()
        play_again()


# Prints the Welcome Message
print()
print("*****  Welcome to Cascais Casino  *****")
player_name = input("What is your name? ")
print("Good luck " + player_name + "\n")


# Main Application Initializes the Player and Dealer and names the Player
player1 = Player()
player1.name = player_name
dealer1 = Dealer()

# Get the initial amount to bet
starting_bet = input("How much money do you want to put in the pot? ")
player1.money = int(starting_bet)
player1.initial_bet = int(starting_bet)

# Starts the game
play_blackjack()


# Things to finish
# 1) Check if there is enough money to bet 
# 2) Check for Aces and if the there is an 
# Ace and Score is over 21 than subtract 10 from score
# 3) Only shuffle cards if there are less than 10 cards left