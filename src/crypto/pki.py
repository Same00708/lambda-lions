from nacl import signing, public


def generate_keypair():
    """Return a new Ed25519 signing and verify key pair."""
    sk = signing.SigningKey.generate()
    vk = sk.verify_key
    return sk, vk


def get_encryption_keys(sk: signing.SigningKey):
    """Convert Ed25519 keys to X25519 (Curve25519) for encryption."""
    epk = sk.verify_key.to_curve25519_public_key()
    esk = sk.to_curve25519_private_key()
    return esk, epk


def get_public_encryption_key(vk: signing.VerifyKey):
    """Convert Ed25519 VerifyKey to X25519 PublicKey."""
    return vk.to_curve25519_public_key()
