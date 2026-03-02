class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Y mi ID de estudiante es {self.student_id}.")

Student1 = Student("Emil", 28, "S12345")
Student1.greet()