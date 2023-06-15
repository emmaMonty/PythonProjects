import sys
from Usage import usage
def sort(args):
    if len(args)<1:
        usage("too few arguments", "sort")
        sys.exit(1)
    lst=[]
    for z in args:
        f =open(z)
        for line in f:
            lst.append(line)
        lst.sort()
        for y in lst:
            print(y, end='')
        f.close()
