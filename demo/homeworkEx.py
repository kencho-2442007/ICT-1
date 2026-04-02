my_tuple =('Hello',123456)
print(type(my_tuple))
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])
a, b = my_tuple
print(b)
new_tup = tuple(a)
print(new_tup)
concatented_tuple = my_tuple + new_tup
print(concatented_tuple)
print(concatented_tuple[2:6:1])
print(concatented_tuple[::-1])
del my_tuple
print(concatented_tuple[::-1][0],concatented_tuple[::-1][4])
