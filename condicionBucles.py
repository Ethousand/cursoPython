#dentro de python exite tambien las condiocionales if, elif y else que modifican el flujo del programa

choice = int(input("escoga un numero del 1 al 10"))

if choice == 5:
    print("tu numero es 5")
elif choice < 5:
    print('tu numero menor menor que 5')
else:
    print('tu numero es mayor que 5')

# las condionales miden si la condicion es verdadera, sin utilizar condicionales lógicas
# tambien pueden anidarse para tener una lógica más compleja

isMember = True

age = int(input('igrese su edad'))

if isMember:
    if age >= 18:
        print('tienes acceso por ser miembro y mayor de edad')
    else:
        print('si eres miembro pero no eres mayor de edad')
else:
    print('no eres miembro, no tienes acceso')

# inicio de bucles
