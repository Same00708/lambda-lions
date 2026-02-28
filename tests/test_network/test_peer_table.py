import os
import pytest
from src.network.peer_table import PeerTable

@pytest.fixture
def temp_db():
    db_path = "test_peers.db"
    if os.path.exists(db_path):
        os.remove(db_path)
    yield db_path
    if os.path.exists(db_path):
        os.remove(db_path)

def test_peer_table_add_get(temp_db):
    table = PeerTable(temp_db)
    node_id = "test_node_id"
    host = "127.0.0.1"
    port = 7777
    last_seen = 123456.789
    
    table.add_peer(node_id, host, port, last_seen)
    
    peer = table.get_peer(node_id)
    assert peer is not None
    assert peer[0] == host
    assert peer[1] == port

def test_peer_table_list(temp_db):
    table = PeerTable(temp_db)
    table.add_peer("node1", "1.1.1.1", 1111, 1.0)
    table.add_peer("node2", "2.2.2.2", 2222, 2.0)
    
    peers = table.list_peers()
    assert len(peers) == 2
    ids = [p[0] for p in peers]
    assert "node1" in ids
    assert "node2" in ids
