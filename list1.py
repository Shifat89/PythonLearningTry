fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    lineElement=line.split()
    for element in lineElement:
        if element not in lst:
            lst.append(element)
lst.sort()
print(lst)