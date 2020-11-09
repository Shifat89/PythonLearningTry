class partyAnimal:
    x=0
    name=""
    def __init__(self):
        print("I'm CONSTRUCTED!")
    #def __init__(self,h):
        #self.name=h
    def __del__(self):
        print("I'm DESTRUCTED!", self.x)
    def party(self):
        self.x=self.x+1
        print("So far Self is: ", self.x)
an=partyAnimal()
an.party()
an.party()
an= 53
print('an is : ', an)
#ay=partyAnimal("45")
#ay.party()