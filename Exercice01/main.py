# Demander le nom à l'utilisateur 
nom = input("Entrez votre nom : ")
# Demander le prénom à l'utilisateur 
age = int(input("Entrez votre âge : "))

def main(nom, age):
    """
    Fonction qui demande le nom et l âge à l utilisateur,
    puis retourne une phrase de présentation.
    """
    # Affiche le nom et l'age de l'utulisateur 
    return f"Bonjour, je m'appelle {nom} et j'ai {age} ans"

# Appelle de la fonction main()
main(nom, age)   