import sys
from Usage import usage
def grep(args):
    """print lines that match patterns"""
    if len(args)<2:
        usage("Please provide a pattern and at least one filename", "grep")
        sys.exit(1)
    string = args[0]
    start = 1
    if args[0] == '-v':
        start = 2
        string = args[1]
    for z in args[start:]:
        f = open(z)
        if args[0] != '-v':
            for line in f:
                if string in line:
                    print(line,end ="")
        else:
            for line in f:
                if string in line:
                    continue
                else:
                    print(line,end ="")
        f.close()

