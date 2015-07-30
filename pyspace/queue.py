
from queue import PriorityQueue
from time import time


class EventPriorityQueue(PriorityQueue):
    """A PriorityQueue which has a second tuple item.
    
    This makes it so events don't need to sort.
    """

    def put(self, event, priority=5):
        """Augment put to handle priorities."""
        super(EventPriorityQueue, self).put((priority, time(), event))

    def get(self):
        """Augment get so we don't have to parse."""
        return super(EventPriorityQueue, self).get()[2]
