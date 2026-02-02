#Orientend Object Programming - POO

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'hola mi nombre es {self.name} y tengo {self.age} años')