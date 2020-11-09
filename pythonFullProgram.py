fname = input("Enter file name: ")
fh = open(fname)

counts=dict()
for lines in fh:
    wordList=lines.split()
    for words in wordList:
        words=words.upper()
        counts[words]=counts.get(words,0)+1
print(counts)

biggestCount=None
biggestCountWord=None
for word,count in counts.items():
    if biggestCount is None or count>biggestCount :
        biggestCount=count
        biggestCountWord=word
print(biggestCountWord,biggestCount)



