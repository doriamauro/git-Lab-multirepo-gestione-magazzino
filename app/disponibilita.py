"""Verifica disponibilita articoli."""

from app.magazzino import GIACENZE

def disponibile(codice, quantita):
    return quantita > 0 and GIACENZE.get(codice, 0) >= quantita
