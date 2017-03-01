from decimal import Decimal, getcontext
import filecmp

probStr = "Prob02"
test=True

getcontext().prec=10

quarter =   Decimal(0.25)
dime =      Decimal(0.10)
nickel =    Decimal(0.05)
penny =     Decimal(0.01)

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

    outfile.write(line)
    num=Decimal(line[1:])
    
    needed=int(num/quarter)
    outfile.write("Quarters={}\n".format(needed))
    finished=needed*quarter
    num=num-finished

    needed=int(num/dime)
    outfile.write("Dimes={}\n".format(needed))
    finished=needed*dime
    num=num-finished

    needed=int(num/nickel)
    outfile.write("Nickels={}\n".format(needed))
    finished=needed*nickel
    num=num-finished

    needed=int(num/penny)
    outfile.write("Pennies={}\n".format(needed))
    finished=needed*penny
    num=num-finished

    ln+=1


outfile.close()
infile.close()

if test:
    if filecmp.cmp(probStr+"JUDG.out.txt", "JudgingOutputs/"+probStr+".out.txt", False):
        print("PASSED")
    else:
        print("FAILED")
