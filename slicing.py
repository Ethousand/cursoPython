a = ['a', 'b', 'c', 'd']
b = a[:]

print(a, '\n', b)

print('luego de slicing')

del a[2]

print(a, '\n', b)
