import utils                       # importe tout le module
from utils import moyenne, est_admis  # importe des fonctions ciblées

notes = [12, 9, 15, 8, 17, 13, 19, 10]
prix = 100
# Utilisation via import complet
rapport = utils.formater_rapport(notes)
print(rapport)

# Utilisation via import ciblé
m = moyenne(notes)
print(f"Moyenne calculée (from import) : {m:.2f}")

# Constante globale
prix_ttc = utils.prix_ttc(prix)
print(f"Prix TTC pour {prix} € HT (taux {utils.TAUX_TVA*100:.0f}%) : {prix_ttc:.2f} €")

# Exemple de test d'admission
note_test = 11
print(f"Admis ? {est_admis(note_test)}")
if __name__ == "__main__":
    print("Exécution depuis app.py")