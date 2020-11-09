largest=None
smallest=None
while True:
    sval=input('Enter a number: ')
    if sval=='done':
        break
    try:
        fval=int(sval)
    except:
        print('Invalid Input')
        continue
    if smallest == None:
        smallest = fval
    elif smallest > fval:
        smallest = fval
    if largest == None:
        largest = fval
    elif largest < fval:
        largest = fval
print("Maximum", largest)
print("Minimum", smallest)