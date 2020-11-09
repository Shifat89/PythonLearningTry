fname = input("Enter file name: ")
fh = open(fname)
count=0
sum=0.0
for i in fh:
    if i.startswith("X-DSPAM-Confidence:"):
        count=count+1
        posStart = i.find(':')
        str= i[posStart + 1:]
        i2 = str.strip()
        i2 = float(i2)
        sum=sum+i2
avg=(sum/count)
print('Average spam confidence:',avg)
