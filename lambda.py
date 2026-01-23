add = lambda a, b: a + b

mult = lambda a, b: a * b 
square = lambda x: x ** 2

print(add(2, 3))     
print(mult(7, 6))    
print(square(5))    

# uso de lmabda para listas

numbers = [1, 2, 3, 4, 5]
cube_numbers = list(map(lambda x: x ** 3, numbers))

print(cube_numbers)
