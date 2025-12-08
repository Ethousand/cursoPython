#ejemplo de listas de datos
conciertos2026 = [  'Too many zoo',
                    'Rammstein',
                    'Chet Faker',
                    'The pillows']

print(conciertos2026)

numbers = [1,2,3,4, 'cinco']

texto = 'hola todos, estoy aprendiendo python'

mix = ['Emil', 1.69, 28, True, [1,2,3,4]]

print(texto)
print('El largo de la cadena es: ', len(texto))
print('El primer elemento de la de lista mix es ', mix[0])
print('El segundo elemento de la de lista mix es ', mix[1])
print('El ultimo elemento de la de lista mix es ', mix[-1])

print(texto[1:10]) #lista desde el indice 1 hasta el 9
print(texto[:5]) #lista desde el indice 0 hasta el 4
print(mix[:]) #lista de todos los elementos 

# metodos para modificar listas
print('la lista de números al principio es: ', numbers)
numbers.append(6) #agrega un elemento al final de la lista
print(numbers)

numbers.insert(1,15.3) #agrega un elemento en la posicion indicada
print(numbers)

numbers.remove('cinco') #elimina el elemento indicado
numbers.pop() #elimina el ultimo elemento
del numbers[0] #elimina el elemento en la posicion indicada

print(numbers)
