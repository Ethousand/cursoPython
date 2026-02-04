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

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def show_available_books(self):
        print("Libros disponibles en la biblioteca:")
        for book in self.books:
            if book.available:
                print(f"- {book.title} por {book.author}")
    
#aplicación de las clases

#creación de libros y usuarios
book1 = Book("Cien Años de Soledad", "Gabriel García Márquez")
book2 = Book("Don Quijote de la Mancha", "Miguel de Cervantes")
book3 = Book("La Iliada", "Homero")
book4 = Book("1984", "George Orwell")

user1 = User("Luis", '001')

#creación de la biblioteca y adición de libros y usuarios
PopularGreek = Library()

PopularGreek.add_book(book1)
PopularGreek.add_book(book2)
PopularGreek.add_book(book3)
PopularGreek.add_book(book4)

PopularGreek.add_user(user1)

#mostrar libros disponibles
PopularGreek.show_available_books()

user1.borrow_book(book1)
user1.borrow_book(book1)
user1.return_book(book1)
