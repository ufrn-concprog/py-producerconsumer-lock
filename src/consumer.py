"""Define the thread that removes one item from a shared buffer."""

from src.buffer import SharedBuffer
from threading import Thread

class Consumer(Thread):
    """A worker thread that consumes one item from a shared buffer.

    Args:
        id: Thread name used in status messages.
        buffer: Shared buffer from which an item is removed.
    """

    def __init__(self, id, buffer):
        """Create a consumer."""
        super().__init__()
        self.name = id
        self.buffer = buffer

    def run(self):
        """Remove one item from the shared buffer."""
        self.buffer.remove()