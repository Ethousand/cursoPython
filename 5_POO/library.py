# Ejemplo de biblioteca simple utilizando POO
# es se divide en ters clases, libro, persona y biblioteca, la biblioteca gestiona tanto libros como personas
# la persona puede tomar prestado y devolver libros de la biblioteca, el libro tiene atributos como titulo y autor

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False

    def return_book(self):
        self.available = True



class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
            print(f"{self.name} ha tomado prestado el libro '{book.title}'")
        else:
            print(f"El libro '{book.title}' no está disponible")
    


    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} ha devuelto el libro '{book.title}'")
        else:
            print(f"{self.name} no tiene el libro '{book.title}' para devolver")

book1 = Book("Cien Años de Soledad", "Gabriel García Márquez")
book2 = Book("Don Quijote de la Mancha", "Miguel de Cervantes")

user1 = User("Luis", '001')

user1.borrow_book(book1)
user1.borrow_book(book1)
user1.return_book(book1)
