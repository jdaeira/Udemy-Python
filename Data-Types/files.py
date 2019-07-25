
myfile = open("test.txt")

print(myfile.read())

myfile.seek(0) # resets the cursor when reading a file

print(myfile.readlines()) # grabs content as a list

myfile.close()

with open("test.txt") as myNewFile:  # don't have to worry about closing the file if opened with the "with" statement
    contents = myNewFile.read()

print(contents)

with open("test.txt", mode='a') as myfile:
    myfile.write("\nFour on Forth")

with open("writeFile.txt", mode = 'w') as file:
    file.write("Writing for the first time!")

with open("writeFile.txt", mode = 'r') as file:
    print(file.read())