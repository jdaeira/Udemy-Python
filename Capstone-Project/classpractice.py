
class Animal():
    def __init__(self):
        self.Animal = ""
        self.dog = Dog()

class Dog():
    def bark(self):
        print("Woof, woof!")


animal = Animal()
animal.dog.bark()