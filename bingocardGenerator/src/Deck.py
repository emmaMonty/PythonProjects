import sys

import Card
import NumberSet


class Deck():
    def __init__(self, cardSize, cardCount, numberMax):
        """Deck constructor"""
        self.cardCount = cardCount
        self.cardArr=[]
        for x in range(self.cardCount):
            self.cardArr.append(Card.Card(x,cardSize,NumberSet.NumberSet(numberMax)))
           
    def getCardCount(self):
        """Return an integer: the number of cards in this deck"""
        return self.cardCount

    def getCard(self, n):
        """Return card N from the deck"""
        card = None
        n -= 1
        if 0 <= n < self.getCardCount():
            card = self.cardArr[n]
        return card

    def print(self, file=sys.stdout, idx=None):
        """void function: Print cards from the Deck

        If an index is given, print only that card.
        Otherwise, print each card in the Deck
        """
        if idx is None:
            for idx in range(1, self.cardCount + 1):
                card = self.getCard(idx)
                card.print(file)
            print('', file=file)
        else:
            self.getCard(idx).print(file)
