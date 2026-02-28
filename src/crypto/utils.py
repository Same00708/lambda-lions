"""Helper routines: HMAC, HKDF, SHA-256."""

import hashlib
import hmac


def sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


def hmac_sha256(key: bytes, data: bytes) -> bytes:
    return hmac.new(key, data, hashlib.sha256).digest()


def hkdf(salt: bytes, ikm: bytes, info: bytes = b"", length: int = 32) -> bytes:
    # simple HKDF using hashlib
    prk = hmac_sha256(salt, ikm)
    okm = b""
    previous = b""
    i = 1
    while len(okm) < length:
        previous = hmac_sha256(prk, previous + info + bytes([i]))
        okm += previous
        i += 1
    return okm[:length]
