
def square(num):
    return num**2

numbers = [1, 2, 3, 4, 5]

for item in map(square,numbers):
    print(item)

print(list(map(square,numbers)))

