import filecmp

probStr = "Prob04"
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
    
    words=line.strip().split("|")

    if words[0] == words[1]:
        outfile.write("{0}|{1} = NOT AN ANAGRAM\n".format(words[0],words[1]))
        ln+=1
        continue
    
    c1=words[0]
    c2=words[1]

    for let in c1:
        if let in c2:
            c2 = c2.replace(let,"", 1)
            
    outfile.write("{0}|{1} = ".format(words[0],words[1]))
    if c2 == "":
        outfile.write("ANAGRAM\n")
    else:
        outfile.write("NOT AN ANAGRAM\n")

    ln+=1


outfile.close()
infile.close()

if test:
    if filecmp.cmp(probStr+"JUDG.out.txt", "JudgingOutputs/"+probStr+".out.txt", False):
        print("PASSED")
    else:
        print("FAILED")
