
try:
    # Want to attempt this code
    # May have an error
    result = 10 + 10
except:
    print("Hey it looks like you aren't adding correctly!")
else:
    print("Add went well!")
    print(result)


try:
    f = open('testfile', 'w')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError: 
# just except: will look for any errors
    print("Hey you have an OS Error")
finally:
    print("I always run")
# finally block of code always runs with or without an exception

def ask_for_int():
    while True:
        try: 
            number3 = int(input("Please provide a number: "))
        except:
            print("Woops! That is not a number")
            continue
        # else will run if there is not an exception
        else: 
            print("Yes thank you")
            print("Your input was {}".format(number3))
            break
        finally:
            print("I am going to ask you again! \n")
            

ask_for_int()