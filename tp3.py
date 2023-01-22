#encoding : utf8
"""Program for creating class Animal that have some common attributes but can also have specific attributes. We can find all the descendant of an
animal and find the parents of a child."""

class Animal():
    def __init__(self, species, age,foot, diet, mother) -> None :
        self.species = species
        self.age = age
        self.foot = foot
        self.diet = diet 
        self.mother = mother
        self.child_id = [] # contains not understandable id ##
        self.children = [] # contains names
        self.descendants = []
        
    def __str__(self) -> str:
        
        return self.species + " Age: " + str(self.age) + "Nb foot: " + str(self.foot) + " Diet: " + str(self.diet)+ " " + str(self.mother) 
    
class  Homme(Animal):
    def set_name(self, name):
        self.name = name 
        
    def __str__(self): #function to print info from Homme()
        return super().__str__() + "\nname : " + self.name

    
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
