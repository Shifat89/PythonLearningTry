import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)
x='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
print(y)
readLine='Jack and Jill went to the hill with a BUCKET of 7 litres!'
foundList=re.findall('J\S+',readLine)
print(foundList)
print("This is a python program with only a print function!")
fname=input('enter file Name: ')
fh=open(fname)
count=0
for line in fh:
    line=line.rstrip()
    if line.find('From ')>=0:
        count=count+1
        print(line)
print(count)

fname=input('enter file Name: ')
fh=open(fname)
count=0
for line in fh:
    line=line.rstrip()
    if re.search('From ',line):
        count=count+1
        print(line)
print(count)


