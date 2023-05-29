class PiggyBank:
    def __init__(self):
        self.__deposit = 0
        self.__smash = False
        self.__balance = 0
# deposit
    def deposit(self,value):
        if (self.__smash == False):
            self.__balance += value
# smash
    def smash(self):
        self.__smash = True
        self.__balance = 0
# getValues
    def getValues(self):
        return self.__balance,self.__smash
#Status function
def printStatus(name, bank):
        balance, broken = bank.getValues()
        print(name,"has $", balance,"and is",("broken" if broken else "not broken"))

#main function
def main():
    p1 = PiggyBank()
    p2 = PiggyBank()
    printStatus("p1",p1)
    p1.deposit(1.25)
    printStatus("p1",p1)
    p1.deposit(6.55)
    printStatus("p1",p1)
    p1.smash()
    printStatus("p1",p1)
    p1.deposit(2.15)
    printStatus("p1",p1)
    p1.__balance=100.0
    p1.__broken=False
    printStatus("p1",p1)

main()
