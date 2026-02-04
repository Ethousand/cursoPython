# Ejercicio de clase, crear una consesionaria de alquiler de coches
# este debe tener una collecion de coches disponibles para alquilar, donde el usuario pueda ver los coches disponibles
# clases principales: Car, Person, Store

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.available = True

    def rent(self):
        if self.available:
            self.available = False

    def return_car(self):
        self.available = True

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.rented_cars = []
    
    def rent_car(self, car):
        if car.available:
            car.rent()
            self.rented_cars.append(car)
            print(f"{self.name} ha alquilado el coche {car.brand} {car.model}")
        else:
            print(f"El coche {car.brand} {car.model} no está disponible")
    
    def return_car(self, car):
        if car in self.rented_cars:
            car.return_car()
            self.rented_cars.remove(car)
            print(f"{self.name} ha devuelto el coche {car.brand} {car.model}")
        else:
            print(f"{self.name} no tiene el coche {car.brand} {car.model} para devolver")
            
class CarRentalStore:
    def __init__(self):
        self.cars = []
        self.users = []

    def add_car(self, car):
        self.cars.append(car)

    def add_user(self, user):
        self.users.append(user)

    def show_available_cars(self):
        print("Coches disponibles para alquilar:")
        for car in self.cars:
            if car.available:
                print(f"- {car.brand} {car.model} ({car.year})")