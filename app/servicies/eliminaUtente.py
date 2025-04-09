from app  import get_db
from app.models import Dipendenti


def eliminaDipendente(id):
    """
    Funzione che elimina un utente in base all  id.
    """

    db = get_db()
    try:
        dipendentiDel = db.query(Dipendenti).filter(Dipendenti.id).all()  # noqa E712

            #funzione cancellamento singolo dipendente


        db.commit()
    except Exception as e:
        print(f"Errore durante la cancellazione degli utenti: {e}")
        db.rollback()
    finally:
        db.close()