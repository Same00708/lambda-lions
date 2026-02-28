"""Web-of-Trust and TOFU (Trust On First Use) utilities."""


def verify_signature(pubkey, message, signature):
    """Verify a message signed with the given public key."""
    from nacl.signing import VerifyKey
    vk = VerifyKey(pubkey)
    return vk.verify(message, signature)


def tofu_check(node_id, known_ids):
    """Simple TOFU: warn if node_id changes after first seen."""
    if node_id in known_ids:
        return True
    known_ids.add(node_id)
    return False
