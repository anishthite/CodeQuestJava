from decimal import Decimal, getcontext, ROUND_HALF_UP
import filecmp

probStr = "Prob06"
test=False

getcontext().prec=10
getcontext().rounding=ROUND_HALF_UP
TWOPLACES = Decimal(10) ** -2

if test:
    outfile=open(probStr+"JUDG.out.txt", "w")
    infile=open("JudgingInputs/"+probStr+".in.txt", "r")
else:
    outfile=open(probStr+".out.txt", "w")
    infile=open(probStr+".in.txt", "r")


school="NONE"

numNext=False
nLeft=0
ln = 0
for line in infile:
    if ln==0:
        ln+=1
        continue
    
    if numNext:
        print(int(line))
        nLeft=int(line)
        numNext=False
    else:
        if nLeft==0:
            school=line.strip()
            print(school)
            numNext=True
        else:
            nLeft-=1
            print(str(nLeft) + " LEFT!")
            

##    for _ in range(int(line)):
##        print(line)
    
    
    ln+=1


outfile.close()
infile.close()

if test:
    if filecmp.cmp(probStr+"JUDG.out.txt", "JudgingOutputs/"+probStr+".out.txt", False):
        print("PASSED")
    else:
        print("FAILED")
