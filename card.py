class Card:

    def __init__(self, suit, id):
        self.id = id
        self.suit = suit

    def __str__(self):
        match id:
            case 1:
                print('Ace of ', suit)
            case 11:
                print('Jack of ', suit)
            case 12:
                print('Queen of ', suit)
            case 13:
                print('King of ', suit)
            case other:
                print(id, ' of ', suit)

# 1 Ace
# 11 Jack
# 12 Queen
# 13 King

