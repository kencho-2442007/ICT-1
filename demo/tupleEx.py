my_tuple=('Hello', 123456)
print(type(my_tuple))
print(my_tuple)
print(my_tuple[1])
a, b= my_tuple
print(b)
new_tup= tuple(a)
print(new_tup)
concatenated_tuple= my_tuple+new_tup
print(concatenated_tuple)
print(concatenated_tuple[2:6:2])
print(concatenated_tuple[::-1])
del my_tuple
print(my_tuple)

