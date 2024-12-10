from datetime import datetime

# Fonction pour calculer l'âge
def calculer_age(annee_naissance):
    annee_actuelle = datetime.now().year
    return annee_actuelle - annee_naissance

# Message de bienvenue
print("Bienvenue dans notre programme Python !")

# Demander le nom de l'utilisateur
nom = input("Quel est votre nom ? ")

# Demander l'année de naissance de l'utilisateur
try:
    annee_naissance = int(input("Quelle est votre année de naissance ? "))
    age = calculer_age(annee_naissance)

    # Afficher le message personnalisé
    print(f"Bonjour {nom}, vous avez environ {age} ans.")
except ValueError:
    print("Veuillez entrer une année valide.")
