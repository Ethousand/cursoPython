# ejemplo de syntaxis básico en Python
# print('hola')
# print('mundo')

# ejemplo de semantica básica en Python
saludo = 'hola mi nombre es'
nombre = 'Emil'
apellido = 'Colina'
edad = 28

# print (saludo)
# print (nombre)

# uso de la función print y sus diferentes argumentos

#print('hola', 'mundo,', 'estoy', 'probando', 'python')
#print('hola' + 'mundo,'+ 'estoy' + 'probando' + 'print')

# uso de parametros dentro de la función print
#print('hola', 'mundo,', 'estoy', 'probando', 'python', sep='---')

# print(saludo, nombre , apellido, end =f' y tengo {edad} años\n')

print('{}: {} {} y tengo {} años'.format(saludo, nombre, apellido, edad))
pi = 3.141592653589793
print ('El valor de pi es {:.2f}'.format(pi))

print('esto es un ejemplo de simbolos especiales: \n nueva línea \n\t tabulación \n\\ barra invertida \n\' comilla simple \n\" comilla doble')
