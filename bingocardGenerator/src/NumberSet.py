import random

class NumberSet():
    def __init__(self, size):
        """NumberSet constructor"""
        self.max = size
        self.randomize()

    def getSize(self):
        """Return an integer: the size of the NumberSet"""
        return len(self.num)

    def get(self, index):
        """Return an integer: get the number from this NumberSet at an index"""
        try:
            return self.num[index]
        except:
            return None

    def randomize(self):
        """void function: Shuffle this NumberSet"""
        self.num = []
        for x in range(1,self.max+1):
            self.num.append(x)
        random.shuffle(self.num)
        

    def getNext(self):
        """Return an integer: when called repeatedly return successive values
        from the NumberSet until the end is reached, at which time 'None' is returned"""
        try:
            return self.num.pop(0)   
        except:
            return None
