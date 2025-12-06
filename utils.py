"""utils.py – Fonctions utilitaires pour la gestion des notes et du calcul de prix."""
TAUX_TVA = 0.2  # 20 %
def moyenne(notes):
    """Renvoie la moyenne d'une liste de notes (0 si liste vide)."""
    if not notes:
        return 0
    return sum(notes) / len(notes)

def est_admis(note, seuil=10):
    """Retourne True si la note est ≥ au seuil (par défaut 10)."""
    return note >= seuil

def prix_ttc(prix_ht, taux=TAUX_TVA):
    """Applique un taux de TVA (20 % par défaut) pour obtenir un prix TTC."""
    return prix_ht * (1 + taux)

def formater_rapport(notes):
    """Construit une petite chaîne de rapport à partir d'une liste de notes."""
    moyenne_classe = moyenne(notes)
    notes_valides = [note for note in notes if est_admis(note)]
    lignes = [
        "=== Rapport des notes ===",
        f"Notes : {notes}",
        f"Moyenne : {moyenne_classe:.2f}",
        f"Nombre d'étudiants admis : {len(notes_valides)}",
    ]
    return "\n".join(lignes)
if __name__ == "__main__":
    print("Tests rapides de utils.py")
    print(moyenne([10, 12, 14]))
    print(formater_rapport([10, 12, 8, 14]))

import utils


notes_calcul = [15, 18, 12]
print(f"Moyenne : {utils.moyenne(notes_calcul)}")


panier = [29.99, 15.50, 8.75]
total_ht = sum(panier)
total_ttc = utils.prix_ttc(total_ht)
print(f"Total TTC : {total_ttc:.2f}€") 


import math
import datetime
import statistics
from typing import List, Tuple, Optional


TAUX_TVA = 0.2  # 20%
SEUIL_ADMISSION = 10.0
PI = math.pi  

def moyenne(notes: List[float]) -> float:
    """
    Renvoie la moyenne d'une liste de notes.
    
    Args:
        notes: Liste de nombres flottants représentant des notes
        
    Returns:
        float: Moyenne des notes (0 si liste vide)
        
    Exemple:
        >>> moyenne([10.0, 12.0, 14.0])
        12.0
    """
    if not notes:
        return 0.0
    return sum(notes) / len(notes)

def est_admis(note: float, seuil: float = SEUIL_ADMISSION) -> bool:
    """
    Retourne True si la note est ≥ au seuil.
    
    Args:
        note: Note à évaluer
        seuil: Seuil d'admission (par défaut SEUIL_ADMISSION)
        
    Returns:
        bool: True si admis, False sinon
        
    Note:
        Le seuil est inclusif (note == seuil → admis)
    """
    return note >= seuil

def prix_ttc(prix_ht: float, taux: float = TAUX_TVA) -> float:
    """
    Applique un taux de TVA pour obtenir un prix TTC.
    
    Args:
        prix_ht: Prix hors taxes
        taux: Taux de TVA à appliquer (par défaut TAUX_TVA)
        
    Returns:
        float: Prix toutes taxes comprises
        
    Raises:
        ValueError: Si prix_ht est négatif
    """
    if prix_ht < 0:
        raise ValueError("Le prix HT ne peut pas être négatif")
    return prix_ht * (1 + taux)

def formater_rapport(notes: List[float]) -> str:
    """
    Construit un rapport formaté à partir d'une liste de notes.
    
    Args:
        notes: Liste de notes à analyser
        
    Returns:
        str: Rapport formaté avec timestamp et statistiques
    """
    moyenne_classe = moyenne(notes)
    notes_valides = [note for note in notes if est_admis(note)]
    mediane = statistics.median(notes) if notes else 0
    ecart_type = statistics.stdev(notes) if len(notes) > 1 else 0
    
    
    maintenant = datetime.datetime.now()
    timestamp = maintenant.strftime("%d/%m/%Y %H:%M:%S")
    
    lignes = [
        f"=== Rapport des notes ({timestamp}) ===",
        f"Notes : {notes}",
        f"Moyenne : {moyenne_classe:.2f}",
        f"Médiane : {mediane:.2f}",
        f"Écart-type : {ecart_type:.2f}",
        f"Nombre d'étudiants admis : {len(notes_valides)}/{len(notes)}",
        f"Taux de réussite : {len(notes_valides)/len(notes)*100:.1f}%" if notes else "N/A",
    ]
    return "\n".join(lignes)


def arrondir_au_demi_superieur(note: float) -> float:
    """
    Arrondit une note au demi supérieur.
    
    Exemple:
        >>> arrondir_au_demi_superieur(12.3)
        12.5
    """
    return math.ceil(note * 2) / 2

def generer_id_unique(prefix: str = "NOTE") -> str:
    """
    Génère un ID unique basé sur le timestamp.
    
    Utilise datetime pour garantir l'unicité.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    return f"{prefix}_{timestamp}"   