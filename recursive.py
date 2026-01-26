
# las funciones recursivas para funcionar necesitan preveer tanto el caso base como el caso recursivo

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print('El factorial de 5 es: ' + str(factorial(5))) # Output: 120

# otro ejemplo: la serie de Fibonacci

def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print('fibonacci de 11: '+ str(fibonacci(11)))

def sumatory(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sumatory(n - 1)
    
print(sumatory(15)) # Output: 55