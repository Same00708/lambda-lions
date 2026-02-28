"""Premium TUI for Archipel P2P Network using Textual."""

import asyncio
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Input, ListView, ListItem, Label, Log
from textual.containers import Container, Horizontal, Vertical
from textual.binding import Binding
from textual.reactive import reactive

from src.core.node import Node
from src.network.peer_table import PeerTable

class ArchipelDashboard(App):
    """A Textual app to manage Archipel Node."""

    CSS = """
    Screen {
        background: #1a1b26;
    }

    #sidebar {
        width: 30%;
        border-right: solid #3b4261;
        background: #16161e;
    }

    #chat-area {
        width: 70%;
    }

    .peer-item {
        padding: 1 2;
        border-bottom: solid #24283b;
    }

    .peer-selected {
        background: #2ac3de;
        color: #1a1b26;
    }

    #msg-log {
        height: 1fr;
        border: solid #3b4261;
        margin: 1;
        background: #1a1b26;
    }

    #input-area {
        height: auto;
        dock: bottom;
        padding: 1;
    }

    Input {
        border: tall #2ac3de;
        background: #16161e;
    }

    Header {
        background: #24283b;
        color: #c0caf5;
        text-style: bold;
    }

    Footer {
        background: #16161e;
    }

    Label {
        padding: 0 1;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit", show=True),
        Binding("c", "connect_manual", "Connect Ad-hoc", show=True),
        Binding("r", "refresh_peers", "Refresh Peers", show=True),
    ]

    selected_peer_id = reactive(None)

    def __init__(self, port=7777, peer=None):
        super().__init__()
        self.port = port
        self.bootstrap_peer = peer
        self.node = None
        self.peer_refresh_task = None

    def on_mount(self):
        """Start the node when the app starts."""
        asyncio.create_task(self.start_node())
        self.peer_refresh_task = self.set_interval(5, self.update_peer_list)

    async def start_node(self):
        """Initialize and start the P2P node."""
        self.node = Node(f"tui-node-{self.port}", tcp_port=self.port, bootstrap_peer=self.bootstrap_peer)
        
        # Monkey patch on_message_received to update TUI
        original_on_message = self.node.on_message_received
        
        def patched_on_message(sender_id, data):
            msg = data.decode(errors='replace')
            self.query_one("#msg-log", Log).write_line(f"[cyan]{sender_id[:8]}[/cyan]: {msg}")
            original_on_message(sender_id, data)
            
        self.node.on_message_received = patched_on_message
        
        await self.node.start()
        self.query_one(Header).query_one(Static).update(f"Archipel Node | ID: {self.node.node_id.hex()[:16]}...")
        self.query_one("#msg-log", Log).write_line("[bold green]System[/bold green]: Node started and ready.")

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Container(id="main-container"):
            with Horizontal():
                with Vertical(id="sidebar"):
                    yield Label("[bold cyan]PEERS DISCOVERED[/bold cyan]", id="peer-header")
                    yield ListView(id="peer-list")
                with Vertical(id="chat-area"):
                    yield Log(id="msg-log", highlight=True, max_lines=1000)
                    yield Container(
                        Input(placeholder="Type message and press Enter...", id="chat-input"),
                        id="input-area"
                    )
        yield Footer()

    def update_peer_list(self):
        """Refresh the list of peers from the database."""
        if not self.node:
            return
            
        peers = self.node.peer_table.list_peers()
        list_view = self.query_one("#peer-list", ListView)
        
        # Store current selection
        current_selection = list_view.index
        
        list_view.clear()
        for node_id, host, port in peers:
            list_view.append(ListItem(Label(f"Node: {node_id[:8]} ({host}:{port})"), id=f"peer-{node_id}"))
            
        if current_selection is not None and current_selection < len(list_view):
            list_view.index = current_selection

    def on_list_view_selected(self, event: ListView.Selected):
        """Update selected peer ID when a list item is chosen."""
        if event.item and event.item.id:
            self.selected_peer_id = event.item.id.replace("peer-", "")
            self.query_one("#msg-log", Log).write_line(f"[bold yellow]Chatting with {self.selected_peer_id[:8]}[/bold yellow]")

    async def on_input_submitted(self, event: Input.Submitted):
        """Handle input for both chat and manual connection."""
        text = event.value.strip()
        if not text:
            return
            
        event.input.value = ""
        
        # Check if we are in "Connect" mode (starts with /connect) or just sending msg
        if text.startswith("/connect "):
            peer_addr = text.replace("/connect ", "")
            self.query_one("#msg-log", Log).write_line(f"[bold yellow]Ad-hoc[/bold yellow]: Connecting to {peer_addr}...")
            try:
                from src.network.tcp_client import TCPClient
                host, port = peer_addr.split(":")
                client = TCPClient(self.node, host, int(port))
                await client.connect() # This will also add it to the table
                await client.close()
                self.query_one("#msg-log", Log).write_line(f"[bold green]Success[/bold green]: Handshake with {peer_addr} complete.")
                self.update_peer_list()
            except Exception as e:
                self.query_one("#msg-log", Log).write_line(f"[bold red]Connect Failed[/bold red]: {e}")
            return

        if not self.selected_peer_id:
            self.query_one("#msg-log", Log).write_line("[bold red]Error[/bold red]: Select a peer first or use [italic]/connect IP:PORT[/italic]")
            return
            
        try:
            self.query_one("#msg-log", Log).write_line(f"[bold green]Me[/bold green]: {text}")
            await self.node.send_to_peer(self.selected_peer_id, text.encode())
        except Exception as e:
            self.query_one("#msg-log", Log).write_line(f"[bold red]Send Failed[/bold red]: {e}")

    def action_connect_manual(self):
        """Prepare the input for manual connection."""
        input_widget = self.query_one("#chat-input", Input)
        input_widget.value = "/connect "
        input_widget.focus()

    async def action_quit(self):
        """Gracefully stop node and exit."""
        if self.node:
            await self.node.stop()
        self.exit()

if __name__ == "__main__":
    app = ArchipelDashboard()
    app.run()
