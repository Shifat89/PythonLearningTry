score = input("Enter Score: ")
s=float(score)

if s<0.0 or s>1.0:
    print("Input out of range!")
    quit()
else:
    if s>= 0.9:
        o='A'
    elif s>= 0.8:
        o='B'
    elif s>=0.7:
        o='C'
    elif s>= 0.6:
        o='D'
    else:
        o='F'
print(o)


