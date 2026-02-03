# Ejemplo de biblioteca simple utilizando POO
# es se divide en ters clases, libro, persona y biblioteca, la biblioteca gestiona tanto libros como personas
# la persona puede tomar prestado y devolver libros de la biblioteca, el libro tiene atributos como titulo y autor

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

