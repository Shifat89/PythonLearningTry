class partyAnimal():
    x=0
    name=""
    def __init__(self, nam):
        self.name =nam
        print(self.name, " Constructed!")
    def party(self):
        self.x= self.x +1
        print(self.name," party count: ", self.x)
class footballFan(partyAnimal):
    points=0
    def touchdown(self):
        self.points= self.points+7
        self.party()
        print(self.name, "points: ", self.points)
s=partyAnimal("Sally")
s.party()
j=footballFan("Jim")
j.party()
j.touchdown()
j.party()