class Junk(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node


class LinkedList(object):
    def __init__(self, data):
        self.head = Node(data)

    def insert(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node

    def print_list(self):
        current = self.head

        while current is not None:
            print(current.get_data())
            current = current.get_next()


def dfs(start, lists=[], depth=0):

    if start is None:
        return None

    try:
        lists[depth].insert(start.val)
    except IndexError:
        lists.append(LinkedList(start.val))

    depth += 1

    dfs(start.left, lists, depth)
    dfs(start.right, lists, depth)

    return lists


if __name__ == '__main__':
    root = Junk(1)
    root.left = Junk(3)
    root.left.left = Junk(2)
    root.left.right = Junk(4)
    root.right = Junk(6)
    root.right.left = Junk(9)
    root.right.left.right = Junk(20)

    arr = dfs(root)
    for a in arr:
        a.print_list()
        print('==========')
