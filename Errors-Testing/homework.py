
# Problem 1

# Handle the exception thrown by the code below by using try and except blocks.
# In [1]:

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("That is TypeError!")


# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-1-c35f41ad7311> in <module>()
#       1 for i in ['a','b','c']:
# ----> 2     print(i**2)

# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

# Problem 2

# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
# In [2]:

try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("This is a ZeroDivisionError!")
finally:
    print("All Done")

# ---------------------------------------------------------------------------
# ZeroDivisionError                         Traceback (most recent call last)
# <ipython-input-2-6f985c4c80dd> in <module>()
#       2 y = 0
#       3 
# ----> 4 z = x/y

# ZeroDivisionError: division by zero

# Problem 3

# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, 
# else block to account for incorrect inputs.
# In [3]:

def ask():
    waiting = True
    while waiting:
        try:
            number = int(input("What is the number you want to square: "))
        except:
            print("That is not a number!")
        else:
            waiting = False

    print("Your number squared is: {}".format(number ** 2))

ask()


