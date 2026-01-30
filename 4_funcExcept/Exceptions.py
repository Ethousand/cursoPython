# print('Hola mundo)

# rest = 10 + '5

try:
    user = int(input("Ingrese un número: "))
    resultado = 100 / user
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError as e:
    print("Error: Debe ingresar un número válido.")
    print(f"Error details: {e}")
else:
    print(f"El resultado es: {resultado}")

'''
def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

print_exception_hierarchy(Exception)
# colecciones de excepciones: https://docs.python.org/3/library/exceptions.html

'''