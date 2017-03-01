import filecmp

probStr = "Prob01"
test=False


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

    num = int(line)
    for i in range(0,num):
        outfile.write("# "*(num-1)+"#\n")

    
    ln+=1
        
outfile.close()
infile.close()

if test:
    if filecmp.cmp(probStr+"JUDG.out.txt", "JudgingOutputs/"+probStr+".out.txt", False):
        print("PASSED")
    else:
        print("FAILED")
