my_list = [4, 7, "Phil", 0]

# create an iterator from the list
iterator = iter(my_list)

# get the first element of the iterator
#print(next(iterator))  # prints 4

# get the second element of the iterator
#print(next(iterator))  # prints 7

# get the third element of the iterator
#print(next(iterator))  # prints Phil

# get the fourth element of the iterator
#print(next(iterator))  # prints 0

for element in iterator:
    print(element)
