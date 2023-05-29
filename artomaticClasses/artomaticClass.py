class Artomat:
    def __init__(self,text1="generic",text2="generic",text3="generic",text4="generic",
                 money=0,hopper=0,bin1=10,bin2=10,bin3=10,bin4=10):
        self.money = (money * .25)
        self.hopper = (hopper * .25)
        self.bin1 = bin1
        self.bin2 = bin2
        self.bin3 = bin3
        self.bin4 = bin4
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
        self.text4 = text4

#print status function
    def printStatus(self):
        print("1.",self.bin1,"packs of", self.text1)
        print("2.", self.bin2, "packs of", self.text2)
        print("3.", self.bin3, "packs of", self.text3)
        print("4.", self.bin4, "packs of", self.text4)
        print("There is $", self.money,"in this machine")
        print("There is $", self.hopper,"in the hopper")
#drop quarter
    def dropQuarter(self):
        print("ching")
        self.hopper += .25

#pull knob
    def pullKnob(self, choice):
# choice 1
        if choice == 1:
            if self.hopper >= .75 and self.bin1 > 0:
                print("A packs of", self.text1, "slides into view")
                self.money +=self.hopper
                self.hopper = 0
                self.bin1 -=1
            else:
                print("(nothing happens)")
##choice 2
        if choice == 2:
            if self.hopper >= .75 and self.bin2 > 0:
                print("A packs of", self.text2, "slides into view")
                self.money += self.hopper
                self.hopper = 0
                self.bin2 -= 1
            else:
                print("(nothing happens)")
# choice 3
        if choice ==3:
            if self.hopper >= .75 and self.bin3 > 0:
                print("A packs of", self.text3, "slides into view")
                self.money += self.hopper
                self.hopper = 0
                self.bin3 -= 1
            else:
                print("(nothing happens)")
#choice 4
        if choice ==4:
            if self.hopper >= .75 and self.bin4 > 0:
                print("A packs of", self.text4, "slides into view")
                self.money += self.hopper
                self.hopper = 0
                self.bin4 -= 1
            else:
                print("(nothing happens)")
#def restock
    def restock(self):
        self.bin1 =10
        self.bin2 =10
        self.bin3 =10
        self.bin4 =10
        self.hopper =0
        self.money = 0
        print("A grouchy-looking attendent shows up, opens the back, fiddles around a bit, closes it, and leaves")
## main()
def main():

    photoMachine = Artomat(text1="Adams",text2="Arbus",text3="Dali",text4="Lange")
    portraitMachine = Artomat(money=212,hopper=2,bin1=1,bin2=0,bin3=8,bin4=10,
                              text1="Picasso",text2="Rembrandt",text3="Van Gogh",text4="Monet")

    photoMachine.printStatus()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.pullKnob(1)
    photoMachine.pullKnob(2)
    photoMachine.dropQuarter()
    photoMachine.pullKnob(2)
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.pullKnob(2)
    photoMachine.printStatus()
    photoMachine.restock()
    photoMachine.printStatus()
    print("----")
    portraitMachine.printStatus()
    portraitMachine.dropQuarter()
    portraitMachine.pullKnob(1)
    portraitMachine.printStatus()

main()
