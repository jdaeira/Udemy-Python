
my_list = [1, 2, 3]

my_mixed_list = ["John", 50, "Jackie"] # lists can have different data types

print(my_list)

print(my_mixed_list)
print(len(my_mixed_list))
print(my_mixed_list[1:])

combined_list = my_list + my_mixed_list # combines the two lists
print(combined_list)

my_mixed_list.append("Honda") # adding items to an array
print(my_mixed_list)
my_mixed_list.pop() #removes the last element from the list or pop(2) removes the index position of 2
print(my_mixed_list)

new_list = ["a", "e", "x", "b", "c"]
num_list = [4, 1, 8, 3]

new_list.sort()
print(new_list)

num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)