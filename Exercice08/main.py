def log_decorator(func):
    """
    Décorateur qui affiche un message avant et après 
    l'exécution d'une fonction
    """
    def encapsulate():
        print("Début de la fonction.")
        func()
        print("Fin de la fonction.")
    return encapsulate

@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

function_test()

