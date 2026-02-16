# ejemplo de herencia en python
# se tomara como ejemplo de la clase anteorior sobre autos y consesionarios
# el consesionario se expandira para ofrecer tanto autos como bicicletas y camiones 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Carli", 28)
person1.greet()