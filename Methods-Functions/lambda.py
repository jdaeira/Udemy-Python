
def square(num):
    return num**2

numbers = [1, 2, 3, 4, 5]

for item in map(square,numbers):
    print(item)

print(list(map(square,numbers)))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "EVEN"
    else:
        return mystring[0]

names = ["Andy", "Eve", "Sally"]

for name in map(splicer, names):
    print(name)

print(list(map(splicer,names)))

# Filters have to return either true or false
def check_even(num):
    return num % 2 == 0

mynums = [1, 2, 3, 4, 5, 6]

for n in filter(check_even, mynums):
    print(n)


def new_square(num):
    return num ** 2

print(new_square(9))


# Lamba expression
lambda num : num ** 2

# Convert check_even function into lambda expression with map
my_list = list(map(lambda num : num ** 2, mynums))
print(my_list)

my_nums = list(filter(lambda num: num % 2 == 0, mynums))
print(my_nums)

my_names = list(map(lambda letter: letter[0], names))
print(my_names)
