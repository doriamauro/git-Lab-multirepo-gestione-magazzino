from app.magazzino import carica_prodotto
from app.disponibilita import disponibile


def test_carico_e_disponibilita():
    carica_prodotto("P01", 10)
    assert disponibile("P01", 3)
    assert not disponibile("P01", 11)
