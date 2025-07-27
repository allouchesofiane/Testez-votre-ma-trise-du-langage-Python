words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
def main(words):
    """
    Affiche une liste de tuples contenant chaque mot d'une liste
    et le nombre de voyelles présentes dans ce mot.
    """
    # Liste de voyelles 
    voyelles = ["a", "e", "i", "o", "u", "y"]
    # Resulat: une liste de tuples avec le mot et le nombre de voyelles
    resultat = [
        (word, len([lettre for lettre in word if lettre in voyelles]))
        for word in words
    ]
    print(resultat)

# Appelle de la fonction
main(words)