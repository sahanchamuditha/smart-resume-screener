from app.core.database import SessionLocal
from app.models.user import UserDB
from app.core.security import hash_password, verify_password


def create_user(username: str, password: str):
    db = SessionLocal()
    user = UserDB(
        username=username,
        hashed_password=hash_password(password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user


def authenticate_user(username: str, password: str):
    db = SessionLocal()
    user = db.query(UserDB).filter(UserDB.username == username).first()
    db.close()

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user
