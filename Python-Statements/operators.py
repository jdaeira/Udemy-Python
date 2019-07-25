
from random import shuffle
from random import randint

for num in range(10): # range is 0 to 10, but not including 10
    print(num)

print("Break in between for loops")

for num in range(3,10): # range is 3 to 10, but not including 10
    print(num)

print("Break in between for loops")

for num in range(0,10,2): # range in 0 to 10, but not including 10 
    print(num)            # that steps every 2 numbers

index_count = 0

for letter in "abcde":
    print("At index {} the letter is {}".format(index_count, letter))
    index_count +=1


word = "abcdef"
for index, letter in enumerate(word): # enumerate creates a tuple where we can get an index and value
    #print(index)
    print(letter)


mylist = [1,2,3]
mylist2 = ["a", "b", "c"]
mylist3 = [100, 200, 300]

for item in zip(mylist, mylist2, mylist3):  # zip joins two or more lists and then use them for tuple unpacking
    print(item)

print(4 in mylist)  # in keyword looks to see if a value is in a list dictionary, etc

print(min(mylist3)) # gets the minimum value of a list
print(max(mylist3))  # gets the maximum value of a list


mylist4 = [1,2,3,4,5,6,7,8,9,10]

shuffle(mylist4)  # shuffle scrambles a list

print(mylist4)

rand = randint(1,10)

print(rand)

num = input("Enter a number here: ") # input will always import as a string
num = int(num) # changes from a string to int
print(type(num))