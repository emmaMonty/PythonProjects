import sys
from Usage import usage
def head(args):
    """output the first part of files"""
    if len(args)<1:
        usage("Number of lines is required", "head")
        sys.exit(1)
    num = 9
    start = 0
    name = True
    if args[0] == '-n':
        # error checks
        if len(args)== 1:
            usage("Number of lines is required", "head")
            sys.exit(1)
        if args[1].isalpha():
            usage("Number of lines is required", "head")
            sys.exit(1)
        num = int(args[1])-1
        start = 2
    if len(args[start:]) == 1:
        name = False
    for file in args[start:]:
        counter = 0
        if(name):
            print("==> {} <==".format(file))
        f = open(file)
        for line in f:
            print(line,end="")
            if counter >= num:
                break
            else:
                counter += 1
        f.close()
        print()


def tail(args):
    """output the last part of files"""
    if len(args)<1:
        usage("to few arguments", "tail")
        sys.exit(1)
    number = 10
    st = 0
    names = True
    if args[0] == '-n':
        #error check
        if len(args)== 1:
            usage("Number of lines is required", "head")
            sys.exit(1)
        if args[1].isalpha():
            usage("Number of lines is required", "head")
            sys.exit(1)
        number = int(args[1])
        st = 2
    if len(args[st:])==1:
        names = False
    for file in args[st:]:
        lst = []
        reversed = []
        counter = 0
        if(names):
            print("==> {} <==".format(file))
        f = open(file)
        for line in f:
            lst.append(line)
        lst.reverse()
        while counter < number:
            reversed.append(lst[counter])
            counter += 1
        reversed.reverse()
        for y in reversed:
            print(y,end="")
        f.close()
        print("\n")

 
