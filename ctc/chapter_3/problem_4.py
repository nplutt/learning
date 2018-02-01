class Queue(object):

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def add(self, value):
        self.stack_1.append(value)

    def remove(self, peek=False):
        value = None

        while len(self.stack_1) >= 1:
            self.stack_2.append(self.stack_1.pop())

        value = self.stack_1.pop() if not peek else self.stack_1[0]

        while len(self.stack_2) > 0:
            self.stack_1.append(self.stack_2.pop())

        return value

    def peek(self):
        return self.remove(True)
