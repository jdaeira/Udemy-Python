
from deck import Deck

class Player():
    
    def __init__(self):
        self.hand = []
        self.hand_score = 0
    
    def add_score(self, added_score):
        self.hand_score += added_score
        return self.hand_score
