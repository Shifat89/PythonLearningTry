largest=-1
smallest=None
count=0
sum=0
flag=False
search=33
print('largest at the begining=',largest)
print('smallest at the begining=',smallest)
print('count at the begining=',count)
print('sum at the begining=',sum)
for n in [9,14,41,5,89,78,33,10]:
    count=count+1
    sum=sum+n
    if search==n:
        flag=True
        pos=count;
    if smallest==None:
        smallest=n
    elif smallest>n:
        smallest=n
    if largest<n:
        largest=n
    #print(largest,n)
print('largest after checking=',largest)
print('smallest after checking=',smallest)
print('total sum =',sum)
print('Total numbers :',count)
if flag==True:
    print("the number",search,'is found at position',pos,'in the array')
else:
    print("the number",search,'is not found at any position in the array')
