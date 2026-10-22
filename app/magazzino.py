"""Gestione magazzino: primo modulo del laboratorio."""

# mappa delle giacenze
GIACENZE = {}

def carica_prodotto(codice, quantita):
    GIACENZE[codice] = GIACENZE.get(codice, 0) + quantita
    return GIACENZE[codice]
