
my_dict = {"key1": "value1", "key2": "value2"}

print(my_dict["key2"])

prices_Lookup = {"apple": 2.99, "oranges": 1.99, "milk": 5.80}

print(prices_Lookup["milk"])

d = {"k1": 123, "k2":[0, 1, 2], "k3":{"insideKey": 100}}

print(d["k1"])
print(d["k2"])
print(d["k2"][1])
print(d["k3"]["insideKey"])

letters = {"char": ["a", "b", "c"]}

letters["char"][2] = letters["char"][2].upper() # changed c to uppercase
#print(letters["char"][2].upper())
print(letters)

d["k4"] = 500 # add a new value to the dictionary
d["k1"] = 1234 # change the value of the key "k1"
print(d)

print(d.keys()) # prints the keys in a dictionary
print(d.values()) # prints the values in a dictionary
print(d.items()) # prints all the items in a dictionary