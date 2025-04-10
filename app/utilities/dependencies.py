from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.utilities.database import get_db
from app.models.dipendenti import Dipendenti
from app.servicies.auth import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(token: str = Security(oauth2_scheme),
                           db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = verify_token(token)
    if payload is None:
        raise credentials_exception

    username = payload.get("sub")
    if username is None:
        raise credentials_exception

    dipendente = db.query(Dipendenti).filter(Dipendenti.username == username).first()  # Modifica per adattare alla tua query
    if dipendente is None:
        raise credentials_exception

    return dipendente