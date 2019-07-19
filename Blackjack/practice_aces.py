
hand = [8, 10, 11, 11]

def get_score():
        score = 0
        for value in hand:
            score += value
        return adjust_aces(score)

def adjust_aces(hand_score):
        for value in hand:
            if hand_score > 21 and value == 11:
                hand_score -= 10                
        return hand_score

print(get_score())

TGREEN =  '\033[32m' # Green Text
print (TGREEN + "This is some green text!")
