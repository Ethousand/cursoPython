# print('Hola mundo)

# rest = 10 + '5

try:
    user = int(input("Ingrese un número: "))
    resultado = 100 / user
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Debe ingresar un número válido.")
else:
    print(f"El resultado es: {resultado}")
