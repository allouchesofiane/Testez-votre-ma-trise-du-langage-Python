class Person:
    """Classe représentant une personne avec un nom et un âge."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_details(self):
        print(f"je m'appelle {self.name} et j'ai {self.age} ans")


class Employee(Person):
    """Classe représentant un employé, héritée de la classe Person"""

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"j'ai un salaire de {self.salary} euros")

employee = Employee("Dupont", 42, 2000)
employee.display_details()

