fname=input('enter file Name: ')
fh=open(fname)
import re
sum=0
for line in fh:
    line=line.rstrip()
    listNumbers=re.findall('[0-9]+',line)
    if len(listNumbers)==0: continue
    for numbers in listNumbers:
        number=int(numbers)
        sum=sum+number
print('Sum :',sum)
