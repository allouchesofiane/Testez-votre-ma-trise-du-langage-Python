students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}
def resultats_etudiant(students):
    """ 
    Affiche les résultats d'un etudiant à partir d'un dictionnaire
    affiche les résulatats ou un message d'erreur
    """
    # Demande à l'etudiant son nom
    Nom_etudiant = input("Entrez le nom de l'étudiant: ")
    # Affiche les resultats ou un message d'erreur
    if Nom_etudiant == 'Alice' or Nom_etudiant == 'Bob' or Nom_etudiant == 'Charlie' :
        print(f"Notes de {Nom_etudiant}")
        for matiere, note in students[Nom_etudiant].items():
            print(f"{matiere} : {note}")
    else :   
        print(f"L'etudiant {Nom_etudiant} n'existe pas dans la liste.")
        return None
    
# Appelle de la fonction resultats_etudiant()
resultats_etudiant(students)