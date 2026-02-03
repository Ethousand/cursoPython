# Ejemplo de biblioteca simple utilizando POO
# es se divide en ters clases, libro, persona y biblioteca, la biblioteca gestiona tanto libros como personas
# la persona puede tomar prestado y devolver libros de la biblioteca, el libro tiene atributos como titulo y autor

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self, user, book):
        if self.available:
            self.available = False
            print(f"El usuario {user} ha tomado prestado el libro {book.title}")
        else:
            print(f"El libro '{book.title}' no está disponible")

    def return_book(self, user, book):
        self.available = True
        print(f"El usuario {user} ha devuelto el libro {book.title}")

