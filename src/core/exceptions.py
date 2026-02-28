"""Custom exceptions for Archipel."""


class ArchipelError(Exception):
    """Base exception for Archipel."""
    pass


class PeerNotFound(ArchipelError):
    """Raised when a peer is not in the routing table."""
    pass


class InvalidPacket(ArchipelError):
    """Raised when packet format is invalid."""
    pass


class CryptoError(ArchipelError):
    """Raised when encryption/decryption fails."""
    pass


class NetworkError(ArchipelError):
    """Raised for network communication errors."""
    pass
