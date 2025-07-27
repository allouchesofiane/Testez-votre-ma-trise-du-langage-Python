
def square(number):
    """Calcule le carré d'un nombre"""
    if isinstance(number,(int,float)):
        return number * number
    else:
        print("Le paramètre doit être un nombre !")
        return None
    
# Appelle de la fonction 
print(square(10))