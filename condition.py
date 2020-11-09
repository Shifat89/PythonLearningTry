x=input("x value is= ")
x=int(x)
if (x>=5):
    print("x greater than or equal to 5!")
    if(x==5):
        print('x is equal to 5')
    else:
        print('x is greater than 5')
else:
    print('x is less than 5!')

no=input('number only!=')
try:
    isNo=float(no)
except:
    isNo=-1

print('number is',isNo)
