import random

class Card(object):
    def __init__(self, suit,  val):
        self.suit = suit
        self.value = val

    def show(self):
        print (f"{self.value} of {self.suit}")


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range (1, 14):
                self.cards.append(Card(s, v))
    
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            
    def drawcard(self):
        return self.cards.pop()


class Player(object):  
    def __init__(self, name):
        self.name = name
        self.hand= []

    def draw(self, drawcard):
        self.hand.append(deck.drawcard()) 
        return self
    
    def showhand(self):
        for card in self.hand:
            card.show()
    
    def discard(self):
        return self.hand.pop()




card = Card("Clubs", 4)
card.show()

deck = Deck()
deck.shuffle()
card = deck.drawcard()
# card.show()

desmond = Player("desmond")
desmond.draw(deck).draw(deck)
desmond.showhand()
desmond.discard()