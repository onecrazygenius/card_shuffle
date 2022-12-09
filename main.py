from logic import Deck

deck = Deck()

def drawCard(numberToDraw):
    for card in deck.drawCard(numberToDraw):
        print (card)

def viewRemainingCards():
    for x in range(len(deck.cards)):
        print(deck.cards[x].__str__())

while (True):
    userInput = input("Draw Cards or View Remaining Cards? ").lower()
    if userInput == "draw cards":
        numberToDraw = int(input("How many cards would you like to draw? "))
        drawCard(numberToDraw)
    elif userInput == "view remaining cards":
        viewRemainingCards()
    else:
        print("Invalid input")
