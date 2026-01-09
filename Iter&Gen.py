# iterador&generador

fruits = ["apple", "banana", "cherry", "strawberry", "raspberry", 'mango', 'grape', 'orange']

speaker = iter(fruits)

print(next(speaker))

# iterador con cadenas de texto

greeting = "Hola Mundo"

speller = iter(greeting)

for letter in speller:
    print(letter)

