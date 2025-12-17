matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matriz)
print('dentro de una matriz podemos extraer filas', matriz[1], 'como datos puntuales', matriz[1][2])

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tupla)

print('tambien podemos extraer datos de una tupla, como por ejemplo el cuarto elemento:', tupla[3])

tupla[0] = 10  # Esto generará un error porque las tuplas son inmutables

#practica de diccionarios
familia = {'Emil': {'apellido': 'Colina',
                    'edad': 28,
                    'altura':1.70},
                    
           'Edward': {'apellido': 'Colina',
                      'edad': 25,
                      'altura':1.75},

            'Oneida': {'apellido': 'Barrios',
                      'edad': 55,
                      'altura':1.60}}