
from deck import Deck
from player import Player
from dealer import Dealer

TGREEN =  '\033[32m' # Green Text
TWHITE = '\033[37m'  # White Text

# Function to Deal the initial cards to the Player and Dealer
def initial_deal(card):
    player1.hand = card.get_cards(1, player1.hand)
    dealer1.hand = card.get_cards(1, dealer1.hand)
    player1.hand = card.get_cards(1, player1.hand)
    dealer1.hand = card.get_cards(1, dealer1.hand)

# Function that check if a player want to continue playing
# Also checks in the beginning if the player has money to bet
# If no money left there is a message and the game quits
def play_again():
    print()
    if player1.money == 0:
            print(f"You have no money left. You lost ${player1.initial_bet}. Better luck next time.\n")
            exit()    
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
            print(f"Congratulations! You won ${check_winnings}!\n")
        else:
            print(f"You lost ${abs(check_winnings)}. Better luck next time.\n")
        exit()

# Function that Starts or continues the game
def play_blackjack():
    move = ""
    bet_money = False

    # Shuffle a new Deck if the count of cards is less than 10
    if len(cards.cardslist) < 11:
        cards.cardslist = []
        cards.shuffle_cards()
        
    # Ask how much to bet in the game
    # Also checks to see if player bet more than he has in the pot
    while bet_money == False:        
        print(f"You have ${player1.money} to bet!\n")
        bet = input("How much is your bet? ")
        player1.bet = int(bet)
        if player1.bet > player1.money:
            print("You don't have that much money to bet. Try Again!")
        else:
            bet_money = True


    # Calls the function to deal the initial cards to the Player and Dealer
    initial_deal(cards)

    # Prints out the Players hand and score
    player1.print_hand()
    print("Your score is: {}\n".format(player1.get_score()))

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
        print(TGREEN + "Blackjack! The House Wins!\n", TWHITE)
        player1.lost_bet()
        play_again()
        
    # Asks the Player if they want to Stand or Hit. Will exit out if Stand is chosen
    # Checks if player goes over 21. If so then Busted message shown and breaks out of the function
    while move != "s":    
        move = input("Do you want to Stand(s) or Hit(h)? ")
        print()
        
        if move == "h":
            player1.hand = cards.get_cards(1, player1.hand)
            player1.print_hand()
            print("Your score is: {}\n".format(player1.get_score()))
            if player1.get_score() > 21:
                print("You Busted!\n")
                dealer1.print_hand()
                print(TGREEN + "Dealer Wins!\n", TWHITE)
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
        print(TGREEN + f"Dealer score is: {dealer1.get_score()}\n", TWHITE) 
        print(TGREEN + "Dealer Busted\n", TWHITE)
        player1.win_bet()
        play_again()
    # Checks to see if the Final result is a Tie
    elif dealer1.get_score() <= 21 and dealer1.get_score() == player1.get_score():
        print(TGREEN + f"Dealer score is: {dealer1.get_score()}\n", TWHITE) 
        print("PUSH\n")
        play_again()
    # Checks to see if the Dealer Wins the game
    elif dealer1.get_score() <= 21 and dealer1.get_score() > player1.get_score():
        print(TGREEN + f"Dealer score is: {dealer1.get_score()}\n", TWHITE) 
        print(TGREEN + "Dealer Wins!", TWHITE)
        player1.lost_bet()
        play_again()
    # Checks to see if the Player Wins the game
    elif dealer1.get_score() <= 21 and dealer1.get_score() < player1.get_score():
        print(TGREEN + f"Dealer score is: {dealer1.get_score()}\n", TWHITE) 
        print("Player Wins!")
        player1.win_bet()
        play_again()



### Main Function Starts Here
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

# Initialize the deck and shuffle the cards
cards = Deck()
cards.shuffle_cards()

# Starts the game
play_blackjack()


# Things to add later on
# 1) Add Doule Down and Card Splits
# 2) Try adding Multiple Players 