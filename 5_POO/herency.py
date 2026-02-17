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
            print(f"el vehiculo {self.brand} ha sido vendido")
            self.available = False
        else:
            print(f"el vehiculo {self.brand} no esta disponible para la venta")

    def check_availability(self):
        return self.available
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

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
