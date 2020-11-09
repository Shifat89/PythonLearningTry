n=input('enter a number: ')
n=int(n)
while n>0:
    print(n)
    n=n-1
print(n)

while True:
    line=input(">>>> ")
    if(line[0]=='#'):
        print("this is a comment line!")
        continue
    elif line=='done':
        break
    else:
        print(line)
print('DONE!!!')

friends=['a','b','c','d']
for friend in friends:
    print('hello',friend)
print("done saying hello to all!!")