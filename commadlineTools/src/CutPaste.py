import sys 
from Usage import usage
def cut(args):
    """remove sections from each line of files"""
    if len(args)<1:
        usage("too few arguments", "cut")
        sys.exit(1)
    #start of cut 
    lst=[]
    start =0
    if args[0] == "-f":
        try:
            start = 2
            for i in args[1].split(','):
                lst.append(int(i))
                if int(i) <= 0:
                    int(',')
        except:
            usage("A comma-separated field specification is required","cut")
            sys.exit(1)
            
    else:
        try:
            lst.append(1)
        except:
            usage("A comma-separated field specification is required","cut")
            sys.exit(1)
    lst.sort()
    for z in args[start:]:
        f =open(z)
        for line in f:
            comma=""
            for l in lst:
                try:
                    print(comma+line.split(",")[l-1].replace("\n",""),end="")
                    comma =","
                except:
                    print("",end ="")
            print()
        f.close()

    

def paste(args):
    if len(args)<1:
        usage("too few arguments", "paste")
        sys.exit(1)
    #start of paste 
    files = []
    largestFile = 0
    for file in args:
        z=open(file)
        files.append(z)
        number = len(z.readlines())
        if number> largestFile:
            largestFile = number
        z.seek(0)
    for i in range(largestFile):
        temp =[]
        for f in files:
           line=f.readline()
           temp.append(line.strip())   
        print(",".join(temp))
    print()
    for f in files:
        z.close()
    
            
 
