class MyClass:
    """
    Classe représentant une personne avec un nom complet.
    """
    def __init__(self, full_name):
        self.full_name = full_name
 
    def display_name(self):
        print("Le nom complet est: ", self.full_name)


class OtherClass:
    """
    Classe représentant une personne avec prénom et nom séparés.
    """

    def __init__(self, first_name, name):
        self.first_name = first_name
        self.name = name
 
    def display_name(self):
        print(f"Nom complet : {self.first_name} {self.name}")
