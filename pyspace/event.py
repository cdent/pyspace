"""
Events, the fundamental message.
"""

class SpaceEvent(object):

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '<%s>: %s' % (self.__class__.__name__, self.data)


class KernelEvent(SpaceEvent):
    """A special event."""
    pass
