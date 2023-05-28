import random
import time

myPts = 0
devilPts = 0
myTurn = True
die = 0
myRndPts = 0
devilRndPts = 0


def printSimpleBoard(die,myPts,devilPts,myRndPts,devilRndPts):

    # die - Integer valued 1-6.  The rolled die value.
    # myPts - Integer valued 0-100. The current saved score of the human player.
    # devilPts - Integer valued 0-100. The current saved score of the devil.
    # myTurn - Boolean value.  True if it is the human player's turn.
    # myRndPts - Integer valued 0-100.  The human's saved score plus points gained that round.
    # devilRndPts - Integer valued 0-100.  The devil's saved score plus points gained that round.

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("my\tthis\tdevil's\tthis")
    print("score\tround\tscore\tround")
    print("  ", myPts, "\t  ", myRndPts, "\t  ", devilPts, "\t  ", devilRndPts)
    print("\t     die")
    print("\t     ", uDie(die))
    print (die)
    print("\n\n")


def uDie(die):

        # die - Integer valued 1-6.  The rolled die value.

     if die == 1: return "\u2680"
     if die == 2: return "\u2681"
     if die == 3: return "\u2682"
     if die == 4: return "\u2683"
     if die == 5: return "\u2684"
     if die == 6: return "\u2685"


def getResponse():
    while True:
        response = input("[r]oll, [p]ass: ")
        if response == "r": break
        if response == "p": break
        if response == "q": break
        print("huh")
    return response


def getDevilResponse():
    if myPts <= devilPts and  devilRndPts - devilPts <21:
        return "r"
    if myPts > devilPts and  devilRndPts - devilPts <30:
        return "r"
    else:
        return "p"


def main():
    myPts = 0
    devilPts = 0
    myTurn = True
    die = 0
    myRndPts = 0
    devilRndPts = 0
    quitPlaying = False
    endGame = False
    printSimpleBoard(die, myPts, devilPts, myRndPts, devilRndPts)

## My Turn ##
    while True:

        while myTurn == True:
            response = getResponse()
            if response == "r":
                die = random.randint(1,6)
                uDie(die)
                print(die)
                if die == 1:
                    myRndPts =0
                    myTurn = False
                else:
                    myRndPts += die
            elif response == "p":
                 myPts += myRndPts
                 myRndPts = 0
                 myTurn = False
            elif response =="q":
                quitPlaying = True
                break
            if myPts + myRndPts >=100:
                print("You win")
                quitPlaying = True
                break
            printSimpleBoard(die, myPts, devilPts, myRndPts, devilRndPts)
        if quitPlaying:
            break
## Devil's code ##
        while myTurn != True:
            print("Devil's turn")
            dv = getDevilResponse()
            if dv == "r":
                die = random.randint(1, 6)
                uDie(die)
                if die == 1:
                    devilRndPts =0
                    myTurn = True
                else:
                    devilRndPts += die
            elif dv == "p":
                devilPts += devilRndPts
                devilRndPts = 0
                myTurn = True
            if devilPts + devilRndPts >= 100:
                print("devil wins")
                endGame = True
                break
            printSimpleBoard(die, myPts, devilPts, myRndPts, devilRndPts)
            time.sleep(2)
        if endGame == True:
            break
main()
