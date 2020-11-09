hrs = input("Enter Hours:")
rph = input("Enter Rate per Hour:")
try:
    h = float(hrs)
    rph = float(rph)
except:
    print("error in input type!try again....")
    quit()
if h>40:
    hExtra=h-40
    rph4Extra = rph * 1.5
    payExtra = hExtra * rph4Extra
    payNormal=40*rph
    pay=payExtra+payNormal
else:
    pay=h*rph
print(pay)

