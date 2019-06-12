
class Dog():
    
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
        
    # OPERATIONS/Actions ---> Methods
    def bark(self, number):
        print("WOOF! My name is {}! and the number is: {}".format(self.name, number))


myDog = Dog("Terrier", "Zoey")
print(myDog.breed)
print(myDog.name)
print(myDog.species)
myDog.bark(3)

