

def simple_gen():
    for x in range(3):
        yield x

for num in simple_gen():
    print(num)

g = simple_gen()
print(g)
# next keywork gets the next value in the function
print(next(g))
print(next(g))
print(next(g))


s = "hello"
# iter keyword converts the "s" string to be iterable
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
