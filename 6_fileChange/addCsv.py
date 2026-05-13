import csv

# paths for the CSV file
data_Db = '6_fileChange/Data.csv'
updated_Db = '6_fileChange/UpdatedData.csv'

new_product = {
                'nombre': 'wireless Charger',
                'modelo': 'WC-100',
                'categoria': 'accesory',
                'precio': 29.99
               }

'''
with open('6_fileChange/Data.csv', mode='a', newline='') as file:
    # file.write('\n') Agrega una nueva línea antes de escribir el nuevo producto
    csv_writer = csv.DictWriter(file, fieldnames = new_product.keys())
    csv_writer.writerow(new_product)
'''
with open('6_fileChange/Data.csv', mode='r', newline='') as file:
    csv_reader = csv.DictReader(file)
    # Obtener los nombres de las columnas eistentes
    fieldnames = csv_reader.fieldnames + ['total_value']
