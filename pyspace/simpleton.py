"""
Simpleton: the basic actor.
"""

import sys

from threading import Thread
from uuid import uuid4

from .event import SpaceEvent, KernelEvent

class Simpleton(Thread):

    accept = []

    def __init__(self, queue, name=None):
        super(Simpleton, self).__init__()
        self.queue = queue
        self.name = name or uuid4().hex

    def run(self):
        while True:
            event = self.queue.get()
            classes = list(event.__class__.__bases__)
            classes.append(event.__class__)
            if any(x in classes for x in self.accept):
                self.process(event)
            else:
                self._reject(event)
            self.queue.task_done()

    def process(self, event):
        pass

    def _reject(self, event):
        #print('%s rejecting %s' % (self.name, event.data))
        self.queue.put(event, priority=1)


class DebugSimpleton(Simpleton):

    accept = [SpaceEvent]

    def process(self, event):
        print('%s has %s' % (self.name, event.data))


class KernelSimpleton(Simpleton):

    accept = [KernelEvent]

    def process(self, event):
        if event.data.startswith('init:'):
            count = event.data.split(':')[1]
            self._init(int(count))

    def _init(self, count):
        for i in range(count):
            debugger = DebugSimpleton(self.queue)
            debugger.daemon = True
            debugger.start()

        while True:
            message = sys.stdin.readline().strip()
            if message == 'quit':
                break
            self.queue.put(SpaceEvent(message))
        

class SpawningSimpleton(DebugSimpleton):

    def process(self, event):
        super(SpawningSimpleton, self).process(event)
        if event.data == 'spawn':
            self.queue.put(SpaceEvent(uuid4().hex))

