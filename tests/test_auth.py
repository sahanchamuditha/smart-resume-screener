from app.core.security import hash_password, verify_password

def test_password_hashing():
    hashed = hash_password("test123")
    assert verify_password("test123", hashed)
