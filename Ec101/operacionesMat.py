#python manera una serie de operaciones matemáticas básicas
A = 10
B = 3

Suma = A + B
Resta = A - B
Multiplicacion = A * B
Division = A / B

print(f'el resultado de las operaciones es:\nSuma: {Suma}\nResta: {Resta}\nMultiplicacion: {Multiplicacion}\nDivision: {Division}')

#ademas de estas, existen otras operaciones matematicas en python
Exponente = A ** B
Modulo = A % B
IntDiv = A // B

print(f'Exponente: {Exponente}\nModulo: {Modulo}\nResultado División Entera: {IntDiv}')

#tambien podemos abreviar las operaciones matematicas con operadores compuestos
''' A += 2  # A = A + 2
    A -= 2  # A = A - 2
    A *= 2  # A = A * 2
    A /= 2  # A = A / 2
    A **= 2 # A = A ** 2
    A %= 2  # A = A % 2
    A //= 2 # A = A // 2    '''

print('\nEjemplo de operaciones iterativas:\n\nEl valor inicial de a es 10')

for i in range(7):
    a = 10
    
    if i == 0 :
        a += 2
    if i == 1 :
        a -= 2
    if i == 2 :
        a *= 2
    if i == 3 :
        a /= 2
    if i == 4 :
        a **= 2
    if i == 5 :
        a %= 2
    if i == 6 :
        a //= 2
    print(f'Valor de a: {a}')

# Ademas de todo esto tenemos operadores de lógicos o booleanos que comparan valores y nos devuelven True o False
print('\nEjemplo de operadores lógicos:\n')

print(f'¿El valor de A es igual al valor de B? : {A == B}')
print(f'¿El valor de A es diferente al valor de B? : {A != B}')
print(f'¿El valor de A es mayor que el valor de B? : {A > B}')
print(f'¿El valor de A es mayor o igual que el valor de B? : {A >= B}')
print(f'¿El valor de A es menor que el valor de B? : {A < B}')
print(f'¿El valor de A es menor o igual que el valor de B? : {A <= B}')

