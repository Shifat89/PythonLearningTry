print("this is first try of function run!!!")
def greet(lang):
    if lang=='es':
        return 'hola'
    elif lang=='fr':
        return 'bonjour'
    elif lang=='bang':
        return 'shagotom'
    else:
        return 'hello'
print(greet('fr'),"France!!!")
print(greet('es'),"Spain!!!")
print(greet('bang'),"Bangladesh!!!")
print(greet('en'),"Extra!!!")

def addNo(a,b):
    sum=a+b
    return sum
print(addNo(6,4))

highValued=max('Hello world')
print(highValued)

