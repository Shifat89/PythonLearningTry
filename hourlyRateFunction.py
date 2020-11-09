def computepay(a,b):
    if h > 40:
        hExtra = h - 40
        rph4Extra = rph * 1.5
        payExtra = hExtra * rph4Extra
        payNormal = 40 * rph
        pay = payExtra + payNormal
        return pay
    else:
        pay = h * rph
        return pay
hrs = input("Enter Hours:")
rph = input("Enter Rate per Hour:")
h = float(hrs)
rph = float(rph)
p=computepay(h,rph)
print("Pay",p)


