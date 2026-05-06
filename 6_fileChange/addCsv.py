import csv

new_product = {
                'nombre': 'wireless Charger',
                'modelo': 'WC-100',
                'categoria': 'accesory',
                'precio': 29.99
               }

with open('Data.csv', mode='a', newline='') as file:
    csv_writer = csv. DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product)