class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, value):
        self.stack.append(value)
        if not self.min or value < self.min[len(self.min) - 1]:
            self.min.append(value)

    def pop(self):
        return_value = self.stack.pop()
        if return_value == self.min[len(self.min) - 1]:
            self.min.pop()

        return return_value

    def minimum(self):
        return self.min[len(self.min) - 1]


if __name__ == "__main__":
    stack = MinStack()

    stack.push(10)
    print(stack.minimum())
    stack.push(5)
    print(stack.minimum())
    stack.push(50)
    print(stack.minimum())
    stack.push(20)
    print(stack.minimum())
    stack.push(1)
    print(stack.minimum())
    print(stack.pop())
    print(stack.minimum())
    print(stack.pop())
    stack.push(2)
    print(stack.minimum())
    print(stack.pop())
