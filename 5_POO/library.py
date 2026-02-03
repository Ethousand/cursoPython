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


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.available:
            book.borrow(self.name, book.title)
            self.borrowed_books.append(book)
            print(f"{self.name} ha tomado prestado el libro '{book.title}'")
        else:
            print(f"El libro '{book.title}' no está disponible")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book(self.name, book.title)
            self.borrowed_books.remove(book)
            print(f"{self.name} ha devuelto el libro '{book.title}'")
        else:
            print(f"{self.name} no tiene el libro '{book.title}' para devolver")