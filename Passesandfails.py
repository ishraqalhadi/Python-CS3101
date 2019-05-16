name = ["Yasmin","Jamie","Dave","Imran","Jenine","Pat"]
marks = ["90","55","39","41","40","85"]

#Enter the names and marks
print "Please type in 6 names and marks:"
for i in range(6):
    print "Enter name", i + 1,
    name[i] = raw_input()
    print "Enter mark", i + 1,
    marks[i] = input()

print
print "These are the passes and fails:"
print

for i in range(6):
    print name[i],":",
    if marks[i] >= 40:
        print "Pass"
    else:
        print "Fail"
