# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers
# if both numbers are even, but returns the greater if one or both numbers are odd

# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    elif a % 2 != 0 or b % 2 != 0:
        return max(a,b)

result = lesser_of_two_evens(2,4)
print(result)


# ANIMAL CRACKERS: Write a function takes a two-word string 
# and returns True if both words begin with same letter

# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(text):
    myAnimalList = list(text.split())
    if myAnimalList[0][0] == myAnimalList[1][0]:
        return True
    else:
        return False


result = animal_crackers("Levelheaded Llama")
print(result)


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 
# or if one of the integers is 20. If not, return False

# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20:
        return True
    elif sum((n1,n2)) == 20:
        return True
    else:
        return False

    
result = makes_twenty(15,5)
print(result)



    