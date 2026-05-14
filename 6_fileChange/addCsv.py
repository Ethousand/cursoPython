import csv
import random

# paths for the CSV file
data_Db = 'Data.csv'
updated_Db = 'UpdatedData.csv'

new_product = {
                'nombre': 'wireless Charger',
                'modelo': 'WC-100',
                'categoria': 'accesory',
                'precio': 29.99
               }

'''
with open(data_Db, mode='a', newline='') as file:
    # file.write('\n') Agrega una nueva línea antes de escribir el nuevo producto
    csv_writer = csv.DictWriter(file, fieldnames = new_product.keys())
    csv_writer.writerow(new_product)
'''
with open(data_Db, mode='r', newline='') as file:
    csv_reader = csv.DictReader(file)
    # Obtener los nombres de las columnas eistentes
    encabezados = csv_reader.fieldnames + ['cantidad'] +  ['total_value']


    with open (updated_Db, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=encabezados)
        csv_writer.writeheader()

        for row in csv_reader:
            row['cantidad'] = random.choice(range(1, 30))
            row['total_value'] = round(float(row['precio']) * int(row['cantidad']), 2)
            csv_writer.writerow(row)
