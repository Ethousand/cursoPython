import csv
with open('Data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)