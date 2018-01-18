from collections import OrderedDict


def run():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['hello'] = 3
    d['grok'] = 4

    for key in d:
        print(key, d[key])

if __name__ == '__main__':
    """
    OrderedDict exactly controls the order of data when iterating.
    Works by maintaining a doubly linked list that orders the keys
    accordingly. The size of these is twice as large as a normal dict.
    """
    run()
