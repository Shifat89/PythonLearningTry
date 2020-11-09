name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhandle = open(name)
hour=list()
hour1=list()
dictionary=dict()
for line in fhandle:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    fromLine=line.split()
    time=fromLine[5]
    time=time.split(':')
    hour.append(time[0])

for words in hour:
    dictionary[words]=dictionary.get(words,0)+1
print(sorted(dictionary.items()))

for hr,count in dictionary.items():
    hour1.append((hr,count))

hour1.sort()
for hr,count in hour1:
    print(hr,count)


