

cardsList = []

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
faces = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", \
         "Nine", "Ten", "Jack", "Queen", "King", "Ace")


def deckCards():
    for suit in suits:
        for face in faces:
            cardsList.append((suit, face))

deckCards()
print(cardsList)
