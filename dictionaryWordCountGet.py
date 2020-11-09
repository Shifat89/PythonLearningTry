counts=dict() #constructing a dictionary named counts
labelNames=['shifat','prova','nishat','kanta','shifat']
for name in labelNames:
    counts[name] = counts.get(name, 0) + 1
    #if name in counts:
        #counts[name]=counts[name]+1
    #else:
        #counts[name]=1
print(counts)

stuff = dict()
print(stuff.get('candy',-1))


