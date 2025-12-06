"""
notes_utils.py – Fonctions utilitaires pour la gestion des notes.
"""

import statistics
from typing import List

SEUIL_ADMISSION = 10.0

def moyenne(notes: List[float]) -> float:
    """Calcule la moyenne d'une liste de notes."""
    if not notes:
        return 0.0
    return sum(notes) / len(notes)

def est_admis(note: float, seuil: float = SEUIL_ADMISSION) -> bool:
    """Détermine si une note est suffisante."""
    return note >= seuil

def statistiques_notes(notes: List[float]) -> dict:
    """Calcule diverses statistiques sur une liste de notes."""
    if not notes:
        return {
            'moyenne': 0.0,
            'mediane': 0.0,
            'ecart_type': 0.0,
            'min': 0.0,
            'max': 0.0
        }
    
    return {
        'moyenne': moyenne(notes),
        'mediane': statistics.median(notes),
        'ecart_type': statistics.stdev(notes) if len(notes) > 1 else 0.0,
        'min': min(notes),
        'max': max(notes),
        'nombre': len(notes)
    }