
mystring = "hello"

mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist)

mylist = [letter for letter in mystring]  # this creates a list of the letters in mystring (list comprehensions)

print(mylist)

mylist = [char for char in "word"]
print(mylist)

mylist = [num for num in range(0,11)]
print(mylist)

mylist = [num**2 for num in range(0,11)]
print(mylist)

mylist = [num for num in range(0,11) if num%2 == 0]
print(mylist)

celcius = [0,10,20,34.5]

fahrenheit = [( (9/5)*temp + 32 ) for temp in celcius]

print(fahrenheit)

mylist = []

for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)

print(mylist)