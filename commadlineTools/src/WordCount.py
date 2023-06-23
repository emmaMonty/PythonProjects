import sys
from Usage import usage
def wc(files):
    if len(files)<1:
        usage("too few arguments", "wc")
        sys.exit(1)
    #start of function
    totalL=0
    totalB=0
    totalW =0
    for z in files:
        f = open(z)
        numL =0
        numB =0
        numW =0
        for line in f:
            numB += len(line)
            x =line.split()
            numW += len(line.split())
            numL += 1
        f.close()
        print(numL, "\t",numW ,"\t",numB,"\t",z)
        if len(files)>1:
            totalL += numL
            totalW += numW
            totalB += numB
    if len(files)>1:
        print(totalL,"\t",totalW,"\t",totalB,"\t","total")


 
