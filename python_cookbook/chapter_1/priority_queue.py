import heapq


class PriorityQueue:
    def __init__(self):
        """
        _queue (list): Holds the queue
        _index (int): Used to ensure that two items with the same priority
                      are processed in the order they are input
        """
        self._queue = []
        self._index = 0
    
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)


def run():
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('hello'), 4)
    q.push(Item('world'), 1)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())


if __name__ == '__main__':
    run()
