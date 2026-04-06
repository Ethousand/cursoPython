# lectura de archivos con el modo 'r' (read)
"""
with open('6_fileChange/tale.txt', 'r', encoding='utf-8') as file:
    for lines in file:
        print(lines.strip())
"""

# escritura de archivos con el modo 'w' (write)
"""
with open('6_fileChange/tale.txt', 'w', encoding='utf-8') as file:
    file.write('\n\nTarea por Emil.\n')
"""

# anexar texto a un archivo con el modo 'a' (append)
with open('6_fileChange/tale.txt', 'a', encoding='utf-8') as file:
    file.write('\n\nTarea por Emil.\n')
