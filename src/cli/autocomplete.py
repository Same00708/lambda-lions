"""Tab completion for CLI."""


def autocomplete_peers(ctx, args, incomplete):
    """Return list of known peer names for tab completion."""
    # would be populated from peer_table
    return ["peer1", "peer2", "peer3"]
