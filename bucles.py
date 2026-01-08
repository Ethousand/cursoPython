# inicio de bucles
'''for i in range(5):
    print('iteracion numero', i)

fruits = ['manzana', 'banana', 'Naranja', 'pera', 'fresa']

for fruit in fruits:
    print('la fruta es:', fruit)
'''
x = 0
while x < 10:
    
    if x == 4:
        x += 1
        continue
    print('el valor de x es:', x)
    x += 1

# practica con la ffrecuencia fibonacci

end = int(input('ingrese cauntos numeros de la secuencia de fibonacci desea ver: '))

def fibonacci(n):
    global sequence
    sequence = []
    a, b = 0, 1
    for i in range (n):
        sequence.append(a)
        a, b = b, a + b

fibonacci(end)
print(f'la cadena de fibonacci hasta el numero {end} es: {sequence}')