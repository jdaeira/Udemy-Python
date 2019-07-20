
from deck import Deck

class Player():
    
    def __init__(self):
        self.name = ""
        self.hand = []
        self.money = 0
        self.initial_bet = 0
        self.bet = 0
        self.hand_score = 0
        self.deck_value = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, \
                           "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
    
    
    # Get the score of the player
    # Checks for value of an Ace and adds only 1 if score > 21
    def get_score(self):
        score = 0
        for _,b in self.hand:
            score += self.deck_value[b]
        return self.adjust_aces(score)

    # Adjusts the score accordingly to aces in the deck
    # Will adjust Ace value as 11 or 1 accordingly
    def adjust_aces(self, hand_score):
        for _,b in self.hand:
            if hand_score > 21 and self.deck_value[b] == 11:
                hand_score -= 10
        return hand_score
    
    # Prints the hand of the player
    def print_hand(self):
        print(f"* {self.name}'s Cards *")
        for suit, face in self.hand:
            print(f"*  {face}  of  {suit}  *")
        print()
    
    # Call if the player wins the bet
    def win_bet(self):
        self.money += self.bet
    
    # Call if the player loses the bet
    def lost_bet(self):
        self.money -= self.bet

 