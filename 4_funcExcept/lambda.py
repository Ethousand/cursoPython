add = lambda a, b: a + b

mult = lambda a, b: a * b 
square = lambda x: x ** 2

print(add(2, 3))     
print(mult(7, 6))    
print(square(5))    

# uso de lmabda para listas

numbers = range(21)
cube_numbers = list(map(lambda x: x ** 3, numbers))

print(cube_numbers)

# uso de lambda para filtrar listas
oddsNumbers = list(filter(lambda x: x%2 != 0, numbers))

print(oddsNumbers)