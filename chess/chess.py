import random


# the chess piece super class
class ChessPiece:
    def __init__(self, color, x, y):
        self.__color = color
        self.__x = x
        self.__y = y

    def color(self):
        return self.__color

    def location(self):
        return (self.__x, self.__y)

    def x(self):
        return self.__x

    def y(self):
        return self.__y

#Pawn
class Pawn(ChessPiece):
    def __init__(self,color,x,y):
        super().__init__(color,x,y)
    def pic(self):
        #print("Pawn")
        if super().color()== "w":
            return '\u2659'
        else:
            return '\u265F'
    def validMove(self, x, y):
        super().location()
        location = super().location()
        if super().color() == "w":
            if y == location[1] - 1 and x == location[0]:
                return True
            else:
                return False
        else:
            if y == location[1] + 1 and x == location[0]:
                return True
            else:
                return False
#Knight
class Knight(ChessPiece):
    def __init__(self,color,x,y):
        super().__init__(color, x, y)
    def pic(self):
        #print("Knight")
        if super().color() == 'w':
            return "\u2658"
        else:
            return "\u265E"
    def validMove(self, x, y):
        super().location()
        location= super().location()
        if x == location[0] + 1 and y == location [1] + 2:
            return True
        elif x == location[0] + 1 and y == location [1] - 2:
            return True
        elif x== location[0] -1 and y == location[1] + 2:
            return True
        elif x ==location [0] -1 and y == location[1]-2:
            return True
        elif x == location[0]+2 and y == location [1] + 1:
            return True
        elif x == location[0]+2 and y == location[1] - 1:
            return True
        elif x == location [0] -2 and y == location[1] +1:
            return True
        elif x == location[0] -2 and y == location [1] -1:
            return True
        else:
            return False
#Queen
class Queen(ChessPiece):
    def __init__(self,color,x,y):
        super().__init__(color, x, y)
    def pic(self):
        #print("Queen")
        if super().color() == 'w':
            return '\u2655'
        else:
            return '\u265B'
    def validMove(self, x, y):
        super().location()
        location = super().location()
#Rook moves
        if x == location[0] + 1 and y == location[1]:
            return True
        elif x == location[0] +2 and y == location[1]:
            return True
        elif x == location[0] +3 and y == location[1]:
            return True
        elif x == location[0] +4 and y == location[1]:
            return True
        elif x == location[0] +5 and y == location[1]:
            return True
        elif x == location[0] + 6 and y == location[1]:
            return True
        elif x == location[0] + 7 and y == location[1]:
            return True
        elif x == location[0] -1 and y == location[1]:
            return True
        elif x == location[0]-2 and y == location[1]:
            return True
        elif x == location[0] -3 and y == location[1]:
            return True
        elif x == location[0] -4 and y == location[1]:
            return True
        elif x == location[0] -5 and y == location[1]:
            return True
        elif x == location[0] - 6 and y == location[1]:
            return True
        elif x == location[0] - 7 and y == location[1]:
            return True
        elif x == location[0] and y == location[1] +1:
            return True
        elif x == location[0] and y == location[1] +2:
            return True
        elif x == location[0] and y == location[1] +3:
            return True
        elif x == location[0] and y == location[1] +4:
            return True
        elif x == location[0] and y == location[1] + 5:
            return True
        elif x == location[0] and y == location[1] +6:
            return True
        elif x == location[0] and y == location[1] +7:
            return True
        elif x == location[0] and y == location[1] -1:
            return True
        elif x == location[0] and y == location[1] -2:
            return True
        elif x == location[0] and y == location[1] -3:
            return True
        elif x == location[0] and y == location[1] -4:
            return True
        elif x == location[0] and y == location[1] - 5:
            return True
        elif x == location[0] and y == location[1] -6:
            return True
        elif x == location[0] and y == location[1] -7:
            return True
#Bishop Moves
        elif x == location[0] + 1 and y == location[1] + 1:
            return True
        elif x == location[0] + 2 and y == location[1] + 2:
            return True
        elif x == location[0] + 3 and y == location[1] + 3:
            return True
        elif x == location[0] + 4 and y == location[1] + 4:
            return True
        elif x == location[0] + 5 and y == location[1] + 5:
            return True
        elif x == location[0] + 6 and y == location[1] + 6:
            return True
        elif x == location[0] + 1 and y == location[1] - 1:
            return True
        elif x == location[0] + 2 and y == location[1] - 2:
            return True
        elif x == location[0] + 3 and y == location[1] - 3:
            return True
        elif x == location[0] + 4 and y == location[1] - 4:
            return True
        elif x == location[0] + 5 and y == location[1] - 5:
            return True
        elif x == location[0] + 6 and y == location[1] - 6:
            return True
        elif x == location[0] - 1 and y == location[1] + 1:
            return True
        elif x == location[0] - 2 and y == location[1] + 2:
            return True
        elif x == location[0] - 3 and y == location[1] + 3:
            return True
        elif x == location[0] - 4 and y == location[1] + 4:
            return True
        elif x == location[0] - 5 and y == location[1] + 5:
            return True
        elif x == location[0] - 6 and y == location[1] + 6:
            return True
        elif x == location[0] - 1 and y == location[1] - 1:
            return True
        elif x == location[0] - 2 and y == location[1] - 2:
            return True
        elif x == location[0] - 3 and y == location[1] - 3:
            return True
        elif x == location[0] - 4 and y == location[1] - 4:
            return True
        elif x == location[0] - 5 and y == location[1] - 5:
            return True
        elif x == location[0] - 6 and y == location[1] - 6:
            return True
        else:
            return False
#King
class King(ChessPiece):
    def __init__(self,color,x,y):
        super().__init__(color, x, y)
    def pic(self):
       # print("King")
        if super().color() == 'w':
            return '\u2654'
        else:
            return '\u265A'
    def validMove(self, x, y):
        super().location()
        location = super().location()
        if x == location[0] + 1 and y == location[1]:
            return True
        elif x == location[0] + 1 and y == location[1] + 1:
            return True
        elif x == location[0] + 1 and y == location[1] - 1:
            return True
        elif x == location[0] -1 and y == location[1]:
            return True
        elif x == location[0] -1 and y == location[1] +1:
            return True
        elif x == location [0] -1 and y == location[1] -1:
            return True
        elif x == location [0] and y == location[1] +1:
            return True
        elif x == location [0] and y == location[1] -1:
            return True
        else:
            return False

#Bishop
class Bishop(ChessPiece):
    def __init__(self,color,x,y):
        super().__init__(color, x, y)
    def pic(self):
       # print("Bishop")
        if super().color() == "w":
            return "\u2657"
        else:
            return "\u265D"
    def validMove(self, x, y):
        super().location()
        location = super().location()
        if x == location[0] + 1 and y == location[1] + 1:
            return True
        elif x == location[0] + 2 and y == location[1] + 2:
            return True
        elif x == location[0] + 3 and y == location[1] +3:
            return True
        elif x == location[0] + 4 and y == location[1] +4:
            return True
        elif x == location[0] + 5 and y == location[1] +5:
            return True
        elif x == location[0] + 6 and y == location[1] +6:
            return True
        elif x == location[0] + 1 and y == location[1] - 1:
            return True
        elif x == location[0] + 2 and y == location[1] - 2:
            return True
        elif x == location[0] + 3 and y == location[1] -3:
            return True
        elif x == location[0] + 4 and y == location[1] -4:
            return True
        elif x == location[0] + 5 and y == location[1] -5:
            return True
        elif x == location[0] + 6 and y == location[1] -6:
            return True
        elif x == location[0] - 1 and y == location[1] + 1:
            return True
        elif x == location[0] - 2 and y == location[1] + 2:
            return True
        elif x == location[0] - 3 and y == location[1] + 3:
            return True
        elif x == location[0] - 4 and y == location[1] + 4:
            return True
        elif x == location[0] - 5 and y == location[1] + 5:
            return True
        elif x == location[0] - 6 and y == location[1] + 6:
            return True
        elif x == location[0] - 1 and y == location[1] - 1:
            return True
        elif x == location[0] - 2 and y == location[1] - 2:
            return True
        elif x == location[0] - 3 and y == location[1] - 3:
            return True
        elif x == location[0] - 4 and y == location[1] - 4:
            return True
        elif x == location[0] - 5 and y == location[1] - 5:
            return True
        elif x == location[0] - 6 and y == location[1] - 6:
            return True
        else:
            return False
#Rook
class Rook(ChessPiece):
    def __init__(self,color,x,y):
        super().__init__(color, x, y)
    def pic(self):
        #print("Rook")
        if super().color() =="w":
            return '\u2656'
        else:
            return '\u265C'
    def validMove(self, x, y):
        super().location()
        location = super().location()
        if x == location[0] + 1 and y == location[1]:
            return True
        elif x == location[0] +2 and y == location[1]:
            return True
        elif x == location[0] +3 and y == location[1]:
            return True
        elif x == location[0] +4 and y == location[1]:
            return True
        elif x == location[0] +5 and y == location[1]:
            return True
        elif x == location[0] + 6 and y == location[1]:
            return True
        elif x == location[0] + 6 and y == location[1]:
            return True
        elif x == location[0] -1 and y == location[1]:
            return True
        elif x == location[0]-2 and y == location[1]:
            return True
        elif x == location[0] -3 and y == location[1]:
            return True
        elif x == location[0] -4 and y == location[1]:
            return True
        elif x == location[0] -5 and y == location[1]:
            return True
        elif x == location[0] - 6 and y == location[1]:
            return True
        elif x == location[0] -7 and y == location[1]:
            return True
        elif x == location[0] and y == location[1] +1:
            return True
        elif x == location[0] and y == location[1] +2:
            return True
        elif x == location[0] and y == location[1] +3:
            return True
        elif x == location[0] and y == location[1] +4:
            return True
        elif x == location[0] and y == location[1] + 5:
            return True
        elif x == location[0] and y == location[1] +6:
            return True
        elif x == location[0] and y == location[1] +7:
            return True
        elif x == location[0] and y == location[1] -1:
            return True
        elif x == location[0] and y == location[1] -2:
            return True
        elif x == location[0] and y == location[1] -3:
            return True
        elif x == location[0] and y == location[1] -4:
            return True
        elif x == location[0] and y == location[1] - 5:
            return True
        elif x == location[0] and y == location[1] -6:
            return True
        elif x == location[0] and y == location[1] -7:
            return True
        else:
            return False

# print a nice picture of the valid moves
# white pawns only move "up" one space
# black pawns only move "down" one space
# other chess pieces move normally
def printValidMoves(cp):
    print("\t  ", cp.pic(), "at", cp.location())
    for i in range(7, -1, -1):
        print("\t" + str(i) + " ", end="")
        for j in range(0, 8):
            if cp.x() == j and cp.y() == i:
                print(cp.pic() + " ", end="")
            elif cp.validMove(j, i):
                print("* ", end="")
            else:
                print(". ", end="")
        print()
    print("\t  ", end="")
    for i in range(0, 8):
        print(str(i) + " ", end="")
    print()
    print()


# returns a random chess piece at a random location
# each of these types must inherit from ChessPiece
def randomChessPiece():
    if random.randint(0, 1) == 0:
        c = "w"
    else:
        c = "b"
    t = random.randint(1, 6)
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    if t == 1: return Pawn(c, x, y)
    if t == 2: return Queen(c, x, y)
    if t == 3: return King(c, x, y)
    if t == 4: return Rook(c, x, y)
    if t == 5:
        return Knight(c, x, y)
    else:
        return Bishop(c, x, y)


def main():
    clist = []

    # make a list of random chess pieces
    for i in range(0, 10):
        clist.append(randomChessPiece())

    # display thier valid moves
    for i in range(0, len(clist)):
        # behold! polymorphism works!
        printValidMoves(clist[i])


main()
