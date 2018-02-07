class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_pivot(length):
    if length == 1:
        return 0

    return length // 2 + length % 2


def bst(arr, start=None, end=None):
    if start == end:
        return None

    mid = start + get_pivot(end - start)
    node = Node(arr[mid])
    node.left = bst(arr, start, mid)
    node.right = bst(arr, mid + 1, end)

    return node


if __name__ == '__main__':
    arr = [1, 3, 6, 7, 9, 10, 15, 16, 20]
    print(bst(arr, 0, len(arr)-1))
