
from deck import Deck

class Player():
    
    def __init__(self):
        self.name = ""
        self.hand = []
        self.money = 0
        self.bet = 0
        self.hand_score = 0
        self.deck_value = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, \
                           "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
    
    # Get the score of the player
    def get_score(self):
        score = 0
        for _,b in self.hand:
            score += self.deck_value[b]
        return score

    # Prints the hand of the player
    def print_hand(self):
        print(f"* {self.name}'s Cards *")
        for suit, face in self.hand:
            print(f"*  {face}  of  {suit}  *")
        print()
    
    # Find out the bet amount 
    def bet_amount(self, bet_table):
        self.bet = bet_table

    # Call if the player wins the bet
    def win_bet(self, bet_table):
        self.money += bet_table
    
    # Call if the player loses the bet
    def lose_bet(self, bet_table):
        self.money -= bet_table
