import sys

import NumberSet


class Card():
    def __init__(self, idnum, size, numberSet):
        """Card constructor"""
        self.size = size
        self.id = idnum
        self.numberSet = numberSet
        self.numArry  = []
        
        for i in range(self.size):
            temp = []
            for j in range(self.size):
                temp.append(self.numberSet.getNext())
            self.numArry.append(temp)
        if self.size%2 != 0:
            self.numArry[int(self.size/2)][int(self.size/2)] = 'Free!'


    def getId(self):
        """Return an integer: the ID number of the card"""
        return self.id

    def getSize(self):
        """Return an integer: the size of one dimension of the card.
        A 3x3 card will return 3, a 5x5 card will return 5, etc.
        """
        return self.size

    def getSquare(self, row, col):
        """Return the value in the Bingo square at (row, col) """
        return self.numArry[row][col]

    


    def print(self, file=sys.stdout):
        #print(self.numArry)
        for i in range(self.size):
            print(("+-----")*self.size + "+",file=file)
            for j in range(self.size):
                if self.numArry[i][j] == "Free!":
                    print("|"+self.numArry[i][j],end ="",file=file)
                else:
                    if self.numArry[i][j] > 99: #don't overcomplicated it....
                        if j == self.size-1:
                            print("|"+" "+ str(self.numArry[i][j]) + " |",file=file)
                        else:
                            print("|"+" "+ str(self.numArry[i][j]) + " ", end ="",file=file)
                    elif self.numArry[i][j] > 9:
                        if j == self.size-1:
                            print("|"+" "+ str(self.numArry[i][j]) + "  |",file=file)
                        else:
                            print("|"+" "+ str(self.numArry[i][j]) + "  ", end ="",file=file)
                    else:
                        if j == self.size-1:
                            print("|"+"  "+ str(self.numArry[i][j]) + "  |",file=file)
                        else:    
                            print("|"+"  "+ str(self.numArry[i][j]) + "  ", end ="",file=file)
        print(("+-----")*self.size + "+",file=file)
        
# test printing card
import sys
if __name__ == "__main__":
    size= int(sys.argv[1])
    card = Card(0,size,NumberSet.NumberSet(size*size*4))
    card.print()
