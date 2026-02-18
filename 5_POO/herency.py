# ejemplo de herencia en python
# se tomara como ejemplo de la clase anteorior sobre autos y consesionarios
# el consesionario se expandira para ofrecer tanto autos como bicicletas y camiones 

class Vehicle:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.available = True

    def sell(self):
        if self.available:
            print(f"El vehiculo {self.brand} ha sido vendido")
            self.available = False
        else:
            print(f"El vehiculo {self.brand} no esta disponible para la venta")

    def check_availability(self):
        return self.available
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

#clases hijos para la super clase Vehicle, cada una con su propia implementación de los métodos para arrancar y detener el motor
class Car(Vehicle):
    def start_engine(self):
        if self.available:
            print(f"El motor del coche {self.brand} {self.model} ha arrancado")
        else:
            print(f"El coche {self.brand} {self.model} no está disponible")

    def stop_engine(self):
        if self.available:
            print(f"El motor del coche {self.brand} {self.model} se ha detenido")
        else:
            print(f"El coche {self.brand} {self.model} no está disponible")

class Bike(Vehicle):

    def start_engine(self):
        if self.available:
            print(f"La bicicleta {self.brand} {self.model} esta en marcha")
        else:
            return f"La bicicleta {self.brand} {self.model} no está disponible"

    def stop_engine(self):
        if self.available:
            return f"La bicicleta {self.brand} {self.model} se ha detenido"
        else:
            return f"La bicicleta {self.brand} {self.model} no está disponible"

class Truck(Vehicle):

    def start_engine(self):
        if self.available:
            print(f"El motor del camión {self.brand} {self.model} ha arrancado")
        else:
            print(f"El camión {self.brand} {self.model} no está disponible")

    def stop_engine(self):
        if self.available:
            print(f"El motor del camión {self.brand} {self.model} se ha detenido")
        else:
            print(f"El camión {self.brand} {self.model} no está disponible")

# clase para los clientes del concesionario
class Costumer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.purchased_vehicles = []

    def inquiring_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            avaliability = "disponible"
        else:
            avaliability = "no disponible"

        print(f"El vehículo {vehicle.brand} {vehicle.model} está {avaliability} para la venta. Precio: ${vehicle.get_price()}")
    
    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
            print(f"{self.name} ha comprado el {vehicle.brand} {vehicle.model}")
        else:
            print(f"El {vehicle.brand} {vehicle.model} no está disponible para la venta")

# clase para el concesionario
class Dealership:
    def __init__(self):
        self.vehicles = []
        self.customers = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehículo {vehicle.brand} {vehicle.model} agregado al inventario")

    def add_customer(self, customer: Costumer):
        self.customers.append(customer)
        print(f"Cliente {customer.name} fue agregado")

    def show_available_vehicles(self):
        print("Vehículos disponibles en el concesionario:")
        for vehicle in self.vehicles:
            if vehicle.check_availability():
                print(f"- {vehicle.brand} {vehicle.model} ({vehicle.year}) - ${vehicle.get_price()}")

# aplicación de las clases
# creación de vehículos
car1 = Car("Toyota", "Corolla", 2020, 20000)
bike1 = Bike("Trek", "X-Caliber", 2021, 15000)
truck1 = Truck("Ford", "F-150", 2022, 35000)

# creación de clientes
customer1 = Costumer("Carlos", "C001")
customer2 = Costumer("María", "C002")

# creación del concesionario
dealership = Dealership()

# agregar vehículos y clientes al concesionario
dealership.add_vehicle(car1)
dealership.add_vehicle(bike1)
dealership.add_vehicle(truck1)

dealership.add_customer(customer1)
dealership.add_customer(customer2)

# mostrar vehículos disponibles
dealership.show_available_vehicles()

# consultar disponibilidad de un vehículo por parte de un cliente
customer1.inquiring_vehicle(car1)
car1.start_engine()
car1.stop_engine()

# comprar un vehículo
customer1.buy_vehicle(car1)