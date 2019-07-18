
from deck import Deck

class Dealer():
    
    def __init__(self):
        self.hand = []
        self.hand_score = 0
        self.deck_value = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, \
                           "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
    
    # Gets the score of the dealer
    # Checks for value of an Ace and adds only 1 if score > 21
    def get_score(self):
        score = 0
        for _,b in self.hand:
            if self.deck_value[b] == 11 and (score + 11) > 21:
                score += 1
            else:                
                score += self.deck_value[b]
        return score

    # Prints the dealers first hand of cards
    def print_first_hand(self):
        # print out the first card and leave the second card blank
        print("* Dealers Cards *")
        print("* First card not shown *")
        print("* " + self.hand[1][1] + " of " + self.hand[1][0] + " *" + "\n")
        
    # Prints out the all the cards in the dealers hand of cards    
    def print_hand(self):
        print("* Dealers Cards *")
        for suit, face in self.hand:
            print(f"*  {face}  of  {suit}  *")
        print()