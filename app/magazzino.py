"""Gestione magazzino: primo modulo del laboratorio."""

GIACENZE = {}

def carica_prodotto(codice, quantita):
    GIACENZE[codice] = GIACENZE.get(codice, 0) + quantita
    return GIACENZE[codice]

    # aggiungo un commento.


# e io qua ci metto un commento