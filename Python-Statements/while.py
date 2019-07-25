
x = 0

while x < 5:
    print(f"The current value of x is {x}")
    x += 1
else:
    print("x is not less than 5")

# break: Breaks out of the current closest enclosing loop.
# continue: Goes to the top of the closest enclosing loop.
# pass: Does nothing at all. Used as a placeholder to avoid syntax error

x = [1,2,3]

for item in x:
    # comment
    pass

mystring = "John"

for letter in mystring:
    if letter == "o":
        continue # Goes back to the for statement without printing the "o"
    print(letter)

for letter in mystring:
    if letter == "o":
        break # breaks out of the loop when letter is "o"
    print(letter)


y = 0

while y < 5:
    if y == 2:
        break
    print(f"The current value of y is {y}")
    y += 1