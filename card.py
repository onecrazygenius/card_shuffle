class Card:

    def __init__(self, suit, id):
        # If suit is not s,d,h,c then return None
        if suit not in ['s','d','h','c']:
            return None
        
        # If the id is not in the range 1 to 14 return None
        if id not in range(1,14):
            return None
        
        self.id = id
        self.suit = suit


    # 1 Ace
    # 11 Jack
    # 12 Queen
    # 13 King
    # Return a string representation of this card object
    def __str__(self):
        match self.id:
            case 1:
                return str('Ace of ' + getSuit(self.suit))
            case 11:
                return str('Jack of ' + getSuit(self.suit))
            case 12:
                return str('Queen of ' + getSuit(self.suit))
            case 13:
                return str('King of ' + getSuit(self.suit))
            case other:
                return str( str(self.id) + ' of ' + getSuit(self.suit))

    def getSuit(suit)
        match suit:
            case 's':
                return 'Spades'
            case 'd':
                return 'Diamonds'
            case 'h':
                return 'Hearts'
            case 'c':
                return 'Clubs'




