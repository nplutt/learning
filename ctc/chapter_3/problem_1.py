class ArrayStack(object):

    def __init__(self):
        self.arr = []
        self.index_1 = 0
        self.index_2 = 0
        self.index_3 = 0

    def get_index(self, stack):
        if stack == 1:
            return self.index_1
        elif stack == 2:
            return self.index_1 + self.index_2
        elif stack == 3:
            return self.index_1 + self.index_2 + self.index_3

    def update_index(self, stack, num):
        if stack == 1:
            self.index_1 += num
        elif stack == 2:
            self.index_2 += num
        elif stack == 3:
            self.index_3 += num

    def push(self, stack, value):
        self.arr.insert(self.get_index(stack), value)
        self.update_index(stack, 1)

    def pop(self, stack):
        import pdb; pdb.set_trace()
        return_value = self.arr.pop(self.get_index(stack) - 1)
        self.update_index(stack, -1)

        return return_value

if __name__ == "__main__":
    stack = ArrayStack()
    stack.push(3, 1)
    stack.push(2, 4)
    stack.push(2, 6)
    stack.push(1, 3)
    stack.push(3, 9)
    stack.push(1, 15)
    print(stack.pop(3))
    print(stack.pop(1))
    print(stack.pop(2))
