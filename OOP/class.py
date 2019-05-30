
class Dog():
    
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        # Is a boolean True/False
        self.spots = spots


myDog = Dog("Poodle", "Chanel", False)
print(myDog.breed)
print(myDog.name)
print(myDog.spots)
