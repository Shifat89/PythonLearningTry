cin=input('text = ')
posStart=cin.find(':')
strLen=len(cin)
#str2=cin[posStart+1:]
str2=cin[posStart+1:strLen]
cin2=str2.strip()
cin2=float(cin2)
print(cin2)

