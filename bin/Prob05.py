from decimal import Decimal, getcontext, ROUND_HALF_UP
import filecmp

probStr = "Prob05"
test=True

getcontext().prec=10
getcontext().rounding=ROUND_HALF_UP
TWOPLACES = Decimal(10) ** -2

if test:
    outfile=open(probStr+"JUDG.out.txt", "w")
    infile=open("JudgingInputs/"+probStr+".in.txt", "r")
else:
    outfile=open(probStr+".out.txt", "w")
    infile=open(probStr+".in.txt", "r")

ln = 0
for line in infile:
    if ln==0:
        ln+=1
        continue
    
    

    outfile.write("Total of the bill: {}\n".format(line.strip()))
    num=Decimal(line[1:])

    outfile.write("15% = ${}\n".format((num*Decimal(.15)).quantize(TWOPLACES)))
    outfile.write("18% = ${}\n".format((num*Decimal(.18)).quantize(TWOPLACES)))
    outfile.write("20% = ${}\n".format((num*Decimal(.20)).quantize(TWOPLACES)))
    
    ln+=1


outfile.close()
infile.close()

if test:
    if filecmp.cmp(probStr+"JUDG.out.txt", "JudgingOutputs/"+probStr+".out.txt", False):
        print("PASSED")
    else:
        print("FAILED")
