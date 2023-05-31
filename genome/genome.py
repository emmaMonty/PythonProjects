

class Genome:
    def __init__(self, sequence ="general"):
        self.sequence = ""
        sequence = sequence.lower()
        for i in range(len(sequence.upper())):
            if sequence[i] == "a":
                self.sequence += sequence[i].upper()
            elif sequence [i] == "c":
                self.sequence += sequence[i].upper()
            elif sequence[i] == "t":
                self.sequence += sequence[i].upper()
            elif sequence[i] == "g":
                self.sequence += sequence[i].upper()
#display
    def display(self):
        print(self.sequence)
#genes
    def genes(self):
        geneStart =0
        for i in range(len(self.sequence)):
            if self.sequence[i:i+3] == "ATG":
                inGene = True
                geneStart=i+3
            if self.sequence[i:i+3] == 'TAG' or self.sequence[i:i+3] == 'TAA' or self.sequence[i:i+3] == 'TGA' and inGene:
                inGene = False
                if i - geneStart >= 3:
                    print(self.sequence[geneStart:i])
        if geneStart == 0:
            print("No gene is found")
def main():

    s1 = Genome("..T.aA.DERRfDww..t.wwWWwwGC..")
    s2 = Genome("TTATGTTTTAAGGATGGGGCGTTAGTT")
    s3 = Genome("TGTGTGTATAT")
    s4 = Genome("TTATGTTTAAGGATGGGGCGTTAGTT")

    s1.display()

    print("---")
    s2.display()
    s2.genes()

    print("---")
    s3.display()
    s3.genes()

    print("---")
    s4.display()
    s4.genes()


main()
