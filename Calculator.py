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



option = input("Selcciones una opción (1.- suma, 2.- resta, 3.- multiplicar, 4.- dividir, 5.- exponencial, 6.- raiz, 7.- salir): ")
