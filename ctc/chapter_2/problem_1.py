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
        self.head = data

    def insert(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node

    def remove_node(self, current, previous=None):
        if previous is not None:
            previous.set_next(current.get_data())
        else:
            self.head = current.get_next()

    def remove_duplicates(self):
        current = self.head
        values = {}
        previous = None

        while current is not None:
            if values.get(current.get_data(), None) is None:
                values[current.get_data()] = current.get_data()

            else:
                self.remove_node(current, previous)

            previous = current
            current = current.get_next()

    def print_list(self):
        current = self.head

        while current is not None:
            print(current.get_data())
            current = current.get_next()

    def find_k_to_last(self, k):
        count = 0
        current = self.head
        previous = None

        while current is not None:
            if count == k:
                previous = self.head

            current = current.get_next()
            previous = previous.get_next()
            count += 1

        return previous

    def delete_middle(self, node):
        if node is None or node.get_next() is None:
            return False

        next = node.get_next()
        node.data = next.data
        node.next = next.next

    def partition(self, value):
        current = self.head
        list_2 = None
        previous = None

        while current is not None:
            if current.get_data() >= value:
                if list_2 is None:
                    list_2 = current
                else:
                    list_2.set_next(current)
                self.remove_node(current, previous)

            previous = current
            current = current.get_next()

        previous.set_next(list_2)


def backwards_sum(linked_list_1, linked_list_2):
    current_1 = linked_list_1.head
    current_2 = linked_list_2.head
    val_1 = ""
    val_2 = ""

    while current_1 is not None:
        val_1 = str(current_1.get_data()) + val_1

    while current_2 is not None:
        val_2 = str(current_2.get_data()) + val_2

    return val_1 + val_2


if __name__ == "__main__":
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)

    ll = LinkedList(node_1)
    ll.insert(node_2)
    ll.insert(node_3)
    ll.insert(node_1)
    ll.insert(node_5)
    ll.insert(node_3)
    ll.insert(node_4)
    ll.insert(node_2)

    # ll.print_list()

    ll.remove_duplicates()
    ll.print_list()
