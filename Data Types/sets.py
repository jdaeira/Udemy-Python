
# Sets have to be unique values

myset = set()

myset.add(1)

print(myset)

myset.add(2)

print(myset)

myset.add(2) # can't put the same value that is already in the set twice

mylist = [1,1,1,2,2,2,3,3,3]

print(set(mylist))

state = "Mississippi"

print(set(state))