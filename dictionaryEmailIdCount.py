#File Open
name = input("Enter file:")
fhandle = open(name)
#construct a dictionary and a list
counts=dict()
email=list()

for line in fhandle: #for every line in file
    line=line.rstrip()
    #check if the line starts with from on not
    if not line.startswith('From '):
        continue
    #split the words of line starting with From
    emailLine=line.split()
    #take only the 2nd word from the split,and make e list of the 2nd elements
    email.append(emailLine[1])
#after the list is made for all lines in file,make a histogram of mail IDs
for id in email:
    counts[id] = counts.get(id, 0) + 1
#maximum find
biggestCount=None
biggestCountedID=None
for key,value in counts.items(): #key-value pairs are in items
    if biggestCount is None or value>biggestCount:
        biggestCount=value
        biggestCountedID=key
print(biggestCountedID,biggestCount)

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])
dir(days)