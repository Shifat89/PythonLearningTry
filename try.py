name = input('Enter File: ')
if len(name)<1: name = 'romeo.txt'
fhand = open(name)
#wordList=list()
lineNo=0
total=0
find = input('Enter the keyword you want to search: ')
for line in fhand:
    wordList=list()
    lineNo=lineNo+1
    line=line.rstrip()
    words=line.split()
    wordCount=0
    for word in words:
        wordCount=wordCount+1
        if(word == find):
           # wordCount=str(wordCount)
            wordList.append(wordCount)
            total=total+1
        else:
            continue
    length=len(wordList)
    if(length>0):
        print(line)
        print('Found in Line no: ', lineNo, "....at positions", str(wordList)[1:-1], end='.\n')
        #print('Found in Line no: ' ,lineNo ,",at positions",sep=' ', *wordList, end='.\n')
        #print('Found in Line no: ', lineNo, ' at positions: ', ', '.join(wordList) )

print('Total : ', total)
