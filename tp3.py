#encoding : utf8
class Animal():
    def set_species(self, species):
        self.species = species
    def __init__(self, species, age, diet) -> None :
        self.species = species
        self.age = age
        self.diet = diet 
        
    def __str__(self) -> str:
        return self.species + " " + str(self.age) + " " + str(self.diet) 
    
class  Homme(Animal):
    def set_name(self, name):
        self.name = name 
    
if __name__ == "__main__" :
    chat = Animal("chat", 3, "ommnivore")
    chat2 = Animal("chat", 3, "ommnivore")
    animal2 = Homme("homme", 23, "omnivore")
    animal2.set_name("Miora")
print(animal2.name)
print(Animal)
print(chat)
print(chat2)

#     animal1 = Animal()