class Animal:
    def __init__(self,name,species):
        self.name =name
        self.species = species
    def make_sound(self, sound):
        print("this animal says {}".format(sound)) 

    def __repr__(self):
        return f"{self.name} is a {self.species}"
    

class Cat(Animal):
    def __init__(self,name,breed,toy):
        super().__init__(name,species="Cat")
        self.breed = breed
        self.toy = toy
    def play(self):
        print(f"{self.name} plays with {self.toy}")


blue = Cat("Blue","Scottish Fold","String")
print(blue)
blue.play()