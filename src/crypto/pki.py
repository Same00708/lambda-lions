"""Ed25519 keypair generation and serialization helpers."""

from nacl import signing


def generate_keypair():
    """Return a new Ed25519 signing and verify key pair."""
    sk = signing.SigningKey.generate()
    vk = sk.verify_key
    return sk, vk
