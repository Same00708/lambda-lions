import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.crypto.pki import generate_keypair

if __name__ == "__main__":
    sk, vk = generate_keypair()
    print(f"Private key: {sk.encode().hex()}")
    print(f"Public key: {vk.encode().hex()}")
    
    with open("node_private.key", "wb") as f:
        f.write(bytes(sk))
    with open("node_public.key", "wb") as f:
        f.write(bytes(vk))
    
    print("Keys saved to node_private.key and node_public.key")
