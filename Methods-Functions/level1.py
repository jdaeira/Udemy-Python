# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

# old_macdonald('macdonald') --> MacDonald

# Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    myname = list(name)
    myname[0] = myname[0].upper()
    myname[3] = myname[3].upper()
    return "".join(myname) 
    

print(old_macdonald('macdonald'))


# MASTER YODA: Given a sentence, return a sentence with the words reversed

# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

# Note: The .join() method may be useful here. The .join() method allows you to join together 
# strings in a list with some connector string. For example, some uses of the .join() method:

# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'

# This means if you had a list of words you wanted to turn back into a sentence, 
# you could just join them with a single space string:

# >>> " ".join(['Hello','world'])
# >>> "Hello world"

def master_yoda(text):
    mytext = text.split()
    return " ".join(mytext[::-1])
    

print(master_yoda('I am home'))

print(master_yoda('We are ready'))


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True

# NOTE: abs(num) returns the absolute value of a number

def almost_there(n):
    if abs(n - 100) <= 10 or abs(n - 200) <= 10:
        return True
    else:
        return False
    
print(almost_there(90))

print(almost_there(104))

print(almost_there(150))

print(almost_there(209))