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

print ("Generador con función:")

def my_generator():
    yield 1
    yield 2
    yield 3

for num in my_generator():
    print(num)
