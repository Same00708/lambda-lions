import os
import pytest
from src.crypto.session import Session

def test_session_encryption_decryption():
    # Generate a random 32-byte key
    key = os.urandom(32)
    session = Session(key)
    
    plaintext = b"Hello, Archipel!"
    
    # Encrypt
    encrypted = session.encrypt(plaintext)
    assert len(encrypted) > len(plaintext)
    
    # Decrypt
    decrypted = session.decrypt(encrypted)
    assert decrypted == plaintext

def test_session_wrong_key():
    key1 = os.urandom(32)
    key2 = os.urandom(32)
    
    session1 = Session(key1)
    session2 = Session(key2)
    
    plaintext = b"Secret data"
    encrypted = session1.encrypt(plaintext)
    
    with pytest.raises(Exception):
        # Should fail authentication (tag verification)
        session2.decrypt(encrypted)
