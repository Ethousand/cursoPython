# Ejemplo de función básica

def greet(name, last_name=""):
    print(f"Hello {name} {last_name}, welcome to python")
    

greet("Emil", "Colina")

greet("Ana")

#calculator.py

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b    
def divide(a, b):
    if b == 0: 
        return "Error: Division by zero is not allowed."
    return a / b
def exponential(a, b):
    return a ** b
def sqrt(a, b= 0.5):
    if a < 0:
        return "Error: Cannot compute square root of a negative number."
    return a ** b



def calculator():
    while True:
        option = input("Selcciones una opción (1.- suma \n 2.- resta \n 3.- multiplicar \n 4.- dividir \n 5.- exponencial \n 6.- raiz \n 7.- salir): ")
        if option == "7":
            print("Saliendo de la calculadora.")
            break
        elif option in ["1", "2", "3", "4", "5", "6"]:
            option = int(option)
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))

            if option == 1:
                result = add(a, b) 
                operation = "suma"
            elif option == 2:
                result = subtract(a, b)
                operation = "resta"
            elif option == 3:
                result = multiply(a, b)
                operation = "multiplicación"
            elif option == 4:
                result = divide(a, b)
                operation = "división"
            elif option == 5:
                result = exponential(a, b)
                operation = "exponencial"
            elif option == 6:
                result = sqrt(a, b)
                operation = "raíz"
            print(f"El resultado de la {operation} es: {result}")
 
        else:
            print("Opción no válida. Intente de nuevo.")
            continue

