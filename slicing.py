a = ['a', 'b', 'c', 'd']
b = a

print(a, '\n', b)

del a[2]

print(a, '\n', b)

print(id(a))
print(id(b))