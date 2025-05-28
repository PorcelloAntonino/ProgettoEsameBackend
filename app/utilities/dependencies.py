from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.utilities.database import get_db
from app.models.dipendenti import Dipendenti
from app.servicies.auth import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(token: str = Security(oauth2_scheme),
                           db: Session = Depends(get_db)):


    payload = verify_token(token)


    username = payload.get("sub")


    dipendente = db.query(Dipendenti).filter(Dipendenti.username == username).first()  # Modifica per adattare alla tua query

    return dipendente