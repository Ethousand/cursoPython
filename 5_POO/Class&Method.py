#Orientend Object Programming - POO
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'hola mi nombre es {self.name} y tengo {self.age} años')

person1 = Person('Emil', 28)
person2 = Person('Carli', 32)

person1.greet()
person2.greet()

'''
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f'Se han depositado {amount}. Nuevo saldo: {self.balance}')
        else:
            print('La cuenta está suspendida. No se pueden realizar depósitos.')
    
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f'Se han retirado {amount}. Nuevo saldo: {self.balance}')
            else:
                print('Fondos insuficientes.')
        else:
            print('La cuenta está suspendida. No se pueden realizar retiros.')
    
    def suspend_account(self):
        self.is_active = False
        print(f'La cuenta de {self.account_holder} ha sido suspendida.')
    
    def activate_account(self):
        self.is_active = True
        print(f'La cuenta de {self.account_holder} ha sido activada.')

account1 = BankAccount('Juan Perez', 1000)
account2 = BankAccount('Ana Gomez', 500)

account1.deposit(200)
account1.suspend_account()
account1.deposit(50)
account1.activate_account()
account1.withdraw(300)

account2.withdraw(100)