
# FIND 33: Given a list of ints, return True if the array 
# contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(nums):
    result = True
    for n in range(len(nums) - 1):
        if nums[n] == 3 and nums[n + 1] == 3:
            result = True
            break
        else:
            result = False
    return result


print(has_33([1, 3, 3]))

print(has_33([1, 3, 1, 3]))

print(has_33([3, 1, 3]))



# PAPER DOLL: Given a string, return a string where for every character 
# in the original there are three characters

# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    newWord = ""
    for letter in text:
        newWord += letter * 3
    return newWord
    

print(paper_doll('Hello'))

print(paper_doll('Mississippi'))



# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or 
# equal to 21, return their sum. If their sum exceeds 21 and there's an eleven,
# reduce the total sum by 10. Finally, if the sum (even after adjustment)
# exceeds 21, return 'BUST'

# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(a,b,c):
    sum = a + b + c
    if a == 11 or b == 11 or c == 11:
        sum -= 10
    
    if sum <= 21:
        return sum
    else:
        return "BUST"
    

print(blackjack(5,6,7))

print(blackjack(9,9,9))

print(blackjack(9,9,11))


# SUMMER OF '69: Return the sum of the numbers in the array, 
# except ignore sections of numbers starting with a 6 and extending to the next 9 
# (every 6 will be followed by at least one 9). Return 0 for no numbers.

# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(arr):
    mylist = list(arr)
    if mylist.__contains__(6):
        six = mylist.index(6)
        nine = mylist.index(9)
        del mylist[six : nine + 1]
        return sum(mylist)
    else:
        return sum(mylist)
    

print(summer_69([1, 3, 5]))

print(summer_69([4, 5, 6, 7, 8, 9]))

print(summer_69([2, 1, 6, 9, 11]))