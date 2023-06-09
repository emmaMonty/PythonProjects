import sys
from Usage import usage
def cat(args):
    """concatenate files and print on the standard output"""
    if len(args)<1:
        usage("too few arguments", "cat")
        sys.exit(1)
    for z in args:
        f = open(z)
        for line in f:
            print(line, end='')
        f.close()


def tac(args):
    """concatenate and print files in reverse"""
    if len(args)<1:
        usage("too few arguments", "tac")
        sys.exit(1)
    for z in args:
        f = open(z)
        lst =[]
        for line in f:
            lst.append(line)
        lst.reverse()
        for y in lst:
            print(y, end='')
        f.close()
