
def myfunc(a,b):
    # Returns 5% of the sum of a and b
    return sum((a,b)) * 0.05

result = myfunc(40,60) 

print(result)

def newfunc(*args):
    # Returns 5% of the sum of a and b
    return sum(args) * 0.05

resultTwo = newfunc(40,60,100,100)

print(resultTwo)


def numfunc(*args):
    for item in args:
        print(item)


numfunc(1,2,3,4,5)