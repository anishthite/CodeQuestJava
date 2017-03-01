import filecmp

probStr = "Prob03"
test=True

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

    sides=[int(thing) for thing in line.strip().split(", ")]
    sides.sort()

    s1=sides[0]
    s2=sides[1]
    s3=sides[2]

    if s1+s2<=s3:
        outfile.write("Not a Triangle\n")
    elif len(sides)<=len(set(sides)):
        outfile.write("Scalene\n")
    elif s1 == s3:
        outfile.write("Equilateral\n")
    else:
        outfile.write("Isosceles\n")

    ln+=1


outfile.close()
infile.close()

if test:
    if filecmp.cmp(probStr+"JUDG.out.txt", "JudgingOutputs/"+probStr+".out.txt", False):
        print("PASSED")
    else:
        print("FAILED")
