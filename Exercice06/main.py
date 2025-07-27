# Fonction calculate_average
def calculate_average(numbers):
    """Calcule la moyenne de la liste de nombres"""
    somme = 0
    for number in numbers:
        somme += number
    moyenne = somme/len(numbers)
    return moyenne 
# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
