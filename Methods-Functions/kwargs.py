

def myfunc(**kwargs):
    if "fruit" in kwargs:
        print("My fruit of choice is {}!".format(kwargs["fruit"]))
    else:
        print("I did not find any fruit here")

myfunc(fruit="Apple", car="Honda", veggie="Lettuce")


def newfunc(*args, **kwargs):

    print("I would like {} {}".format(args[0], kwargs["food"]))

newfunc(10,20,30, fruit="Orange", food="Pizza")


