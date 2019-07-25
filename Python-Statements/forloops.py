
greeting = "Hello John!"

for letter in greeting:
    print(letter)

myList = []

for letter in greeting:
    (myList.append(letter))

print(myList)

myNumList = [1,2,3,4,5,6,7,8,9,10]

for num in myNumList:
    print(num)


for num in myNumList:
    if num % 2 == 1:
        print(num)
    else:
        print("Even number: {}".format(num))

list_sum = 0

for num in myNumList:
    list_sum = list_sum + num

print(list_sum)

myList = [(1,2),(3,4),(5,6),(7,8)] # a list of Tuples

for item in myList:
    print(item)

for a,b in myList: #tuple unpacking
    print(a)
    print(b)

dict = {"k1":1, "k2":2, "k3":3}

for key, value in dict.items():
    print(value)

    