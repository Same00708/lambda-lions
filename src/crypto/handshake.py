import hashlib
from nacl.public import PrivateKey, PublicKey, Box


class Handshake:
    def __init__(self, local_private_key: PrivateKey):
        """Initialize with local X25519 PrivateKey."""
        self.local_private = local_private_key

    def derive_session_key(self, remote_public_key: PublicKey) -> bytes:
        """Derive 32-byte session key from remote X25519 PublicKey."""
        # Compute shared secret (X25519)
        shared_secret = Box(self.local_private, remote_public_key).shared_key()
        
        # Simple KDF: SHA-256 of the shared secret
        return hashlib.sha256(shared_secret).digest()
