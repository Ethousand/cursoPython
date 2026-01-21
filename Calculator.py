# Ejemplo de función básica

def greet(name, last_name=""):
    print(f"Hello {name} {last_name}, welcome to python")
    

greet("Emil", "Colina")

greet("Ana")

#calculator.py


def calculator():
    while True:
        option = input("Selcciones una opción: \n 1.- suma \n 2.- resta \n 3.- multiplicar \n 4.- dividir \n 5.- exponencial \n 6.- raiz \n 7.- salir --> ")
        if option == "7":
            print("Saliendo de la calculadora.")
            break
        elif option in ["1", "2", "3", "4", "5", "6"]:
            option = int(option)
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: ")) if option != "6" else 0.5

            if option == 1:
                add = lambda a, b: a + b
                result = add(a, b)
                operation = "suma"

            elif option == 2:
                subtract = lambda a, b: a - b
                result = subtract(a, b)
                operation = "resta"

            elif option == 3:
                multiply = lambda a, b: a * b
                result = multiply(a, b)
                operation = "multiplicación"

            elif option == 4:
                divide = lambda a, b: "Error: Division by zero is not allowed." if b == 0 else a / b
                result = divide(a, b)
                operation = "división"
            
            elif option == 5:
                exponential = lambda a, b: a ** b
                result = exponential(a, b)
                operation = "exponencial"
            
            elif option == 6:
                sqrt = lambda a, b: "Error: Cannot compute square root of a negative number." if a < 0 else a ** b
                result = sqrt(a, 1/b)
                operation = "raíz"
            print(f"\nEl resultado de la {operation} es: {result} \n")
 
        else:
            print("Opción no válida. Intente de nuevo.")
            continue

calculator()