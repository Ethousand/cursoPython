import csv

new_product = {
                'nombre': 'wireless Charger',
                'modelo': 'WC-100',
                'categoria': 'accesory',
                'precio': 29.99
               }

'''
with open('6_fileChange/Data.csv', mode='a', newline='') as file:
    file.write('\n')  # Agrega una nueva línea antes de escribir el nuevo producto
    csv_writer = csv.DictWriter(file, fieldnames = new_product.keys())
    csv_writer.writerow(new_product)
'''
