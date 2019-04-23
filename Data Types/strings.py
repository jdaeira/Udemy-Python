
x = "Hello World!"

print(x.lower())
print(x.upper())
print(x.split())

my_name = "John"
my_age = 50
print("Hello " + my_name)

text = "Hello {}, you are {} years old!".format(my_name, my_age)

print(text)
print("The {2} {1} {0}!".format("fox", "brown", "quick"))
# You can choose which index you want to use
print("The {q} {b} {f}!".format(f = "fox", b = "brown", q = "quick"))

result = 100/777
print("The result is {r:1.3f}".format(r = result))
# r is value:width.precision(how many places) f

print(f"The result is {result:1.3f}")
# f-strings()formatted string literals

print(f"Hello {my_name}, you are {my_age} years old!")