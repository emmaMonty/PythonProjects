def printChoices():
    print("s:Report the machine status")
    print("d:Drop in the quarter")
    print("1: Choice one")
    print("2: Choice two")
    print("3: Choice three")
    print("4: Choice four")
    print("r : Restock the machine")
    print("q: quit")


def main():
    printChoices()

    hopper = 0
    total = 25.25
    choice = 5
    choice2 = 0
    choice3 = 10
    choice4 = 7

    while True:
        response = input()
        if response == "r":
            print("A grumpy man comes to restock the machine.")
            hopper = 0
            total = 0
            choice = 10
            choice2 = 10
            choice3 = 10
            choice4 = 10
        elif response == "q":
            break

        elif response == "s":
            print("1:", choice, "packs of Stan Lee drawings")
            print("2:", choice2, "packs of Frank Miller drawings")
            print("3:", choice3, "packs of  Jim Lee drawings")
            print("4:", choice4, "packs of Jack Kirby drawings")
            print("There is $", total, "in the machine")

        elif response == "d":
            total = total + .25
            print("ching.")
            hopper = hopper + 1
            print("hopper value:", hopper * .25)

        elif response == "1":
            if hopper == 3 and choice > 0:
                print("A pack of Stan Lee drawings dropped")
                choice -= 1
                hopper = 0
            elif hopper == 3 and choice == 0:
                print("Machine makes noise but nothing drops")
                hopper = 0
            else:
                print("nothing happens")
        elif response == "2":
            if hopper == 3 and choice2 > 0:
                print("A pack of Frank Miller drawings dropped")
                choice2 -= 1
                hopper = 0
            elif hopper == 3 and choice2 == 0:
                print("Machine makes noise but nothing drops")
                hopper = 0
            else:
                print("nothing happens")
        elif response == "3":
              if hopper == 3 and choice3 > 0:
                print("A pack of Jim Lee drawings dropped")
                choice3 -= 1
                hopper = 0
              elif hopper == 3 and choice3 == 0:
                print("Machine makes noise but nothing drops")
                hopper = 0
              else:
                  print("nothing happens")
        elif response == "4":
            if hopper == 3 and choice4 > 0:
                print("A pack of Jack Kirby drawings dropped")
                choice4 -= 1
                hopper = 0
            elif hopper == 3 and choice4 == 0:
                print("Machine makes noise but nothing drops")
                hopper = 0
            else:
                print("nothing happens")
        else:
            print("I don't understand")


main()
