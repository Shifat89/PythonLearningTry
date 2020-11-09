fname = input("Enter file name: ")
fh = open(fname)
lst = list()
count=0
for line in fh:
    line1=line.rstrip()
    #guardian rule
    if len(line1)<1:
        continue
    if line1.startswith('From '):
        word=line1.split()
        count=count+1
        print(word[1])
print("There were", count, "lines in the file with From as the first word")