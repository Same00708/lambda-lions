# Archipel Testing Guide

This document explains how to test the different components of the Archipel P2P network.

## 1. Automated Unit Tests
We use `pytest` for automated testing of individual modules (cryptography, peer table, etc.).

**Command:**
```powershell
python -m pytest tests/
```

- Tests are located in the `tests/` directory.
- `tests/test_crypto/test_session.py`: Verifies AES-256-GCM encryption/decryption.
- `tests/test_network/test_peer_table.py`: Verifies SQLite peer storage logic.

---

## 2. Local P2P Connectivity Tests (Manual)
To test the real-world behavior of nodes on a single machine, run multiple instances using different ports.

### Step-by-Step Scenario:
1. **Launch Node A** (Listener):
   ```powershell
   python main.py --port 7777
   ```
2. **Launch Node B** (Bootstrap):
   ```powershell
   python main.py --port 7778 --peer 127.0.0.1:7777
   ```
3. **Observation**:
   - Node B should log: `Connecting to 127.0.0.1:7777...` and `Secure session established`.
   - Node A should log: `Incoming connection from ('127.0.0.1', <port>)` and `Secure session established`.

---

## 3. CLI Command Tests
You can use the CLI tool to manually test parts of the protocol without running a full node.

- **Manual Connect**: Connect to a running node and perform a handshake.
  ```powershell
  python src/cli/commands.py connect --port 8888 --peer 127.0.0.1:7777
  ```
- **Send Message**: Send an encrypted message to a node by its ID.
  ```powershell
  python src/cli/commands.py send --peer-id <NODE_ID_HEX> --message "Secret test message"
  ```
- **List Peers**: View the discovered peers in a node's database.
  ```powershell
  python src/cli/commands.py peers --port 7777
  ```

---

## 4. LAN Tests (Multi-PC)
1. **Identify IP**: Find your PC's LAN IP (e.g., `192.168.1.15`).
2. **Firewall**: Ensure the port (default 7777) is open in the Windows Firewall.
3. **PC A**: `python main.py --port 7777`
4. **PC B**: `python main.py --port 7777 --peer <IP_OF_PC_A>:7777`
