#Coprehension list
squares = [x**2 for x in range(10)]
print(squares)

#convert Celsius to fahrenheit

celcius = [0, 10, 20, 34.5]
farenheit = [(temp*9/5) + 32 for temp in celcius]
print(farenheit)

# extracción de numeros pares

limit = int(input("Enter the limit: "))
evens = [x for x in range(limit+1) if x%2 == 0]
print(evens)

# matriz transpuesta a traves de la comprensión de listas
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(matrix)
print(transposed)