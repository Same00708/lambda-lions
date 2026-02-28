"""End-to-end encrypted chat."""


class Chat:
    def __init__(self, local_node):
        self.local_node = local_node
        self.messages = []

    def send_message(self, recipient_id, plaintext):
        """Send an E2E encrypted message to a peer."""
        # encrypt with recipient's public key
        pass

    def receive_message(self, sender_id, encrypted_data):
        """Decrypt and store an incoming message."""
        # decrypt with local private key
        pass
