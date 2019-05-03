
# SPY GAME: Write a function that takes in a list of integers and 
# returns True if it contains 007 in order

# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    newList = []
    for index in range(len(nums)):
        if nums[index] == 0 or nums[index] == 7:
            newList.append(nums[index])
    bond = "".join(str(num) for num in newList)
    if bond == "007":
        return True
    else:
        return False

print(spy_game([1,2,4,0,0,7,5]))

print(spy_game([1,0,2,4,0,5,7]))

print(spy_game([1,7,2,0,4,5,0]))




# COUNT PRIMES: Write a function that returns the number of prime numbers 
# that exist up to and including a given number

# count_primes(100) --> 25

# By convention, 0 and 1 are not prime.

def count_primes(number):

    primes = 0

    for count in range(2,number):
        if count > 1:
            for num in range(2, count):
                if count % num == 0:
                    break
            else:
                primes += 1
    return primes


print(count_primes(100))



# PRINT BIG: Write a function that takes in a single letter, 
# and returns a 5x5 representation of that letter

# print_big('a')

# out:   *  
#       * *
#      *****
#      *   *
#      *   *

# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
# For purposes of this exercise, it's ok if your dictionary stops at "E".

def print_big(letter):

    letters = {"a":
               "  *  \n"
               " * * \n"
               "*****\n"
               "*   *\n"
               "*   *\n",
               "b":
               "**** \n"
               "*   *\n"         
               "*****\n" 
               "*   *\n"
               "**** \n",
               "c":
               " ****\n"
               "*    \n"
               "*    \n"
               "*    \n"
               " ****\n", 
               "d":
               "**** \n"
               "*   *\n"
               "*   *\n"
               "*   *\n"
               "**** \n",
               "e":
               "*****\n"
               "*    \n"
               "***  \n"
               "*    \n"
               "*****\n"            
              }

    return letters[letter]
    

print(print_big('e'))



        

