# lectura de archivos con el modo 'r' (read)

lines = []
with open('6_fileChange/tale.txt', 'r', encoding='utf-8') as file:
    for line in file:
        lines.append(line.strip())
        print(line.strip())
        print(str(len(lines)) + " lineas leidas\n\n")

print("el archivo tiene " + str(len(lines)) + " lineas en total.")

# escritura de archivos con el modo 'w' (write)
"""
with open('6_fileChange/tale.txt', 'w', encoding='utf-8') as file:
    file.write('\n\nTarea por Emil.\n')
"""

# anexar texto a un archivo con el modo 'a' (append)
'''
with open('6_fileChange/tale.txt', 'a', encoding='utf-8') as file:
    file.write('\n\nTarea por Emil.\n')
'''
