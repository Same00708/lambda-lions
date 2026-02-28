# QUICK REFERENCE - Archipel Development Guide

## 🚀 Common Tasks

### Setup Development Environment
```bash
python -m venv venv
source venv/bin/activate  # or: venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Generate Ed25519 Keys
```bash
python scripts/generate_keys.py
# Creates: node_private.key, node_public.key
```

### Create a 50MB Test File
```bash
python scripts/generate_test_file.py
# Creates: test_50mb.bin
```

### Run Main Node
```bash
python main.py
```

### Run Tests
```bash
pytest tests/
pytest tests/ --cov=src         # With coverage
pytest tests/test_crypto/       # Specific test module
```

---

## 📦 Module Reference

### Crypto (`src/crypto/`)
```python
from src.crypto.pki import generate_keypair
sk, vk = generate_keypair()  # Ed25519

from src.crypto.session import Session
session = Session(key=b'32-byte-key')
ciphertext = session.encrypt(plaintext)
plaintext = session.decrypt(ciphertext)

from src.crypto.utils import sha256, hmac_sha256, hkdf
```

### Network (`src/network/`)
```python
from src.network.peer_table import PeerTable
peers = PeerTable()
peers.add_peer(node_id, host, port, time.time())
peer_info = peers.get_peer(node_id)

from src.network.tcp_server import TCPServer
server = TCPServer(host='0.0.0.0', port=7777)
await server.start()

from src.network.tcp_client import TCPClient
reader, writer = await TCPClient.connect(host, port)
```

### Transfer (`src/transfer/`)
```python
from src.transfer.chunking import chunk_file, write_chunk
for chunk in chunk_file('large_file.bin'):
    # Process chunk

from src.transfer.manifest import Manifest
manifest = Manifest(filename='file.bin', file_hash='sha256...', total_size=1000000)
manifest.to_json()

from src.transfer.storage import Storage
storage = Storage('chunks.db')
storage.store_chunk(hash, filename, index, data)
data = storage.get_chunk(hash)
```

### Messaging (`src/messaging/`)
```python
from src.messaging.chat import Chat
chat = Chat(node)
chat.send_message(recipient_id, plaintext)
chat.receive_message(sender_id, encrypted_data)

from src.messaging.gemini import GeminiIntegration
gemini = GeminiIntegration(api_key='...')
response = gemini.query("What is P2P?")
```

### Protocol (`src/protocol/`)
```python
from src.protocol.packet import Packet
from src.protocol.types import MSG, HELLO

packet = Packet(pkt_type=MSG, node_id=b'...', payload=data)
serialized = packet.serialize()

packet = Packet.deserialize(serialized)
```

### Core (`src/core/`)
```python
from src.core.node import Node
node = Node(node_name='my-node')

from src.core.config import Config
config = Config()
if config.is_gemini_available():
    # Use Gemini API

from src.core.logger import setup_logging
logger = setup_logging(level='DEBUG')
logger.info("Message")
```

### CLI (`src/cli/`)
```python
from src.cli.commands import cli
from src.cli.ui import info, warn, error, success

info("Informational message")
success("Operation successful")
warn("Warning message")
error("Error message")
```

---

## 🔌 Architecture Patterns

### Packet Structure
```
┌─────────┬──────┬──────────┬──────────────┐
│ MAGIC   │ TYPE │ NODE_ID  │ PAYLOAD_LEN  │
│ 0xAA55  │ 1B   │ 32 bytes │ 4 bytes      │
│ CCDD    │      │          │              │
└─────────┴──────┴──────────┴──────────────┘
│       ENCRYPTED PAYLOAD (variable)       │
└────────────────────────────────────────────
│   HMAC-SHA256 (32 bytes)                 │
└────────────────────────────────────────────
```

### Async Pattern (asyncio)
```python
import asyncio

async def main():
    # Create tasks
    task = asyncio.create_task(async_function())
    
    # Wait for completion
    result = await task
    
    # Gather multiple tasks
    results = await asyncio.gather(task1, task2, task3)

asyncio.run(main())
```

### Database Pattern (SQLite)
```python
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS table_name ...''')
conn.commit()
cursor.close()
conn.close()
```

---

## 📁 File Naming Conventions

| Pattern | Usage | Example |
|---------|-------|---------|
| `xyz.py` | Implementation | `pki.py`, `session.py` |
| `test_xyz.py` | Unit tests | `test_pki.py` |
| `*_constants.py` | Configuration | `network_constants.py` |
| `*_utils.py` | Helper functions | `crypto_utils.py` |

---

## 🔍 Debugging Tips

### Enable Debug Logging
```python
from src.core.logger import setup_logging
logger = setup_logging(level='DEBUG')
```

### Check Peer Table
```python
from src.network.peer_table import PeerTable
peers = PeerTable()
print(peers.list_peers())
```

### Inspect Packets
```python
from src.protocol.packet import Packet
try:
    packet = Packet.deserialize(data)
    print(f"Type: {packet.type}, NodeID: {packet.node_id.hex()}")
except ValueError as e:
    print(f"Invalid packet: {e}")
```

### Test Cryptography
```bash
python -c "
from src.crypto.pki import generate_keypair
sk, vk = generate_keypair()
print(f'Public key: {vk.encode().hex()[:32]}...')
"
```

---

## 🐛 Common Issues

### ModuleNotFoundError
**Problem**: `ModuleNotFoundError: No module named 'src'`  
**Solution**: Run from project root: `cd /path/to/archipel && python main.py`

### Port Already in Use
**Problem**: `OSError: [Errno 48] Address already in use`  
**Solution**: Change TCP_PORT in `.env` or kill process using port 7777

### Missing Dependencies
**Problem**: ImportError for crypto, click, rich, etc.  
**Solution**: `pip install -r requirements.txt`

### Multicast Not Working
**Problem**: Peers not discovering each other  
**Solution**: 
- Check firewall allows UDP 6000
- Verify network interface has multicast enabled
- Test with: `python -c "import socket; print(socket.has_ipv6)"`

---

## 📚 Learning Resources

- **Noise Protocol**: https://noiseprotocol.org
- **PyNaCl Docs**: https://pynacl.readthedocs.io
- **AsyncIO**: https://docs.python.org/3/library/asyncio.html
- **SQLite**: https://docs.python.org/3/library/sqlite3.html
- **Click CLI**: https://click.palletsprojects.com

---

## 🎯 Development Workflow

1. **Clone & Setup**
   ```bash
   git clone <repo>
   cd archipel
   python -m venv venv && source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature
   ```

3. **Write Tests First**
   ```bash
   touch tests/test_feature/test_your_module.py
   ```

4. **Implement Feature**
   ```bash
   vim src/module/your_module.py
   ```

5. **Run Tests**
   ```bash
   pytest tests/test_feature/ -v
   ```

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "feat: add your feature"
   git push origin feature/your-feature
   ```

---

**Happy Coding! 🚀**  
*Questions? Check the README.md or open an issue.*
