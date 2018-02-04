class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_pivot(length):
    return length // 2 if length % 2 == 0 else length // 2 + 1


def bst(arr, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(arr)

    mid = start + get_pivot(end - start)
    node = Node(arr[mid])
    node.left = bst(arr, start, mid)
    node.right = bst(arr, mid + 1, end)
    return node
