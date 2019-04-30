

from random import randint

firstNames = ["John", "Chris", "Tom", "Mike", "Andy"]

lastNames = ["Lee", "Anderson", "Williams", "White", "Miller"]

first = randint(0, len(firstNames) - 1)
last = randint(0, len(lastNames) - 1)

print(firstNames[first])
print(lastNames[last])

print("Your fake name is: {} {}".format(firstNames[first], lastNames[last]))