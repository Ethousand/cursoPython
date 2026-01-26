
# las funciones recursivas para funcionar necesitan preveer tanto el caso base como el caso recursivo

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)