import csv

# Lectura regular en forma de diccionario
'''
with open('6_fileChange/Data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
         print(row)
'''

with open('6_fileChange/Data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Nombre: {row['nombre']}, Precio: {row['precio']}")