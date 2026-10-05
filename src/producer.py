"""Define the thread that produces one random item for a shared buffer."""

from src.buffer import SharedBuffer
from random import randint
from threading import Thread

class Producer(Thread):
    """A worker thread that generates and inserts one integer.

    Args:
        id: Thread name used in status messages.
        buffer: Shared buffer that receives the generated item.
    """

    def __init__(self, id, buffer):
        """Create a producer."""
        super().__init__()
        self.name = id
        self.buffer = buffer
        
    def run(self):
        """Generate an integer from 1 through 100 and insert it."""
        item = randint(1, 100)
        self.buffer.insert(item)