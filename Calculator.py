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
            



