# iterador&generador

fruits = ["apple", "banana", "cherry", "strawberry", "raspberry", 'mango', 'grape', 'orange']

speaker = iter(fruits)

print(next(speaker))

# iterador con cadenas de texto

greeting = "Hola Mundo"

speller = iter(greeting)

for letter in speller:
    print(letter)

# generador con función

print ("función generadora:")

def my_generator():
    yield 1
    yield 2
    yield 3

for num in my_generator():
    print(num)

# ejemplo de fibonacci con generador

limit = int(input('Ingrese el límite para la secuencia de Fibonacci: '))

def fibonacci_gen(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

for number in fibonacci_gen(limit):
    print(number)