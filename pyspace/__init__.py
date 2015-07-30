"""Initial module."""

import sys

from .queue import EventPriorityQueue
from .event import KernelEvent
from .simpleton import KernelSimpleton

def main_loop():
    """Not a loop any more. Confusing!"""

    bus = EventPriorityQueue(maxsize=50)
    x = KernelSimpleton(bus, name='kernel')
    x.daemon = True
    x.start()
    bus.put(KernelEvent('init:10'), priority=1)

    # Exit when the queue is empty and the Kernel has stopped.
    bus.join()
