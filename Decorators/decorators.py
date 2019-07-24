

def hello(name = "John"):
    print("The hello() function has been executed!")

    def greet():
        return "\t This is the greet() function inside hello!"

    def welcome():
        return "\t This is the welcome() function inside hello!"

    print("I am going to return a function!!")

    if name == "John":
        return greet
    else:
        return welcome


def cool():

    def super_cool():
        return "I am very cool!"

    return super_cool


greeting = hello()
print(greeting())

some_func = cool()
print(some_func())