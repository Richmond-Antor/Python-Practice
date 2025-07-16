


class Avengers:
    def fight(self):
       print("Avengers, start fighting !!!")

    def retreat(self):
        print("Avengers retrerat for now") 
ironman = Avengers()
hulk = Avengers()

ironman.fight()

#introducing method

class Avengers:
    def introduce(self,name):
        print(f"I am {name} and i protect the world")
# #OBJECT
ironman= Avengers()

thor = Avengers()

ironman.introduce("Tony Stark")

thor.introduce("Thor")

#defualt constructor

class Avenger:
    def __init__(self):
       print("A new Avenger has joined the team")
    
captain = Avenger()    #doesnt have to call seperately

#parameteraized constructor

class Avenger:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def show(self):
        print(f"{self.name} has power: {self.power}")

spiderman = Avenger("spiderman", "Web Slinging")
spiderman.show()

