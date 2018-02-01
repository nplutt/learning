class SetOfStacks(object):

    def __init__(self, max_size):
        self.stacks = []
        self.max_size = max_size
        self.open_stacks = []

    def push(self, value):
        if len(self.open_stacks) == 0:
            self.stacks.append([])

        stack_index = self.open_stacks[len(self.open_stacks) - 1]
        self.stacks[stack_index].append(value)

        if len(self.stacks[stack_index]) - 1 >= self.max_size:
            self.open_stacks.pop()

    def pop(self):
        stack_index = self.open_stacks[len(self.open_stacks) - 1]
        value = self.stacks[stack_index].pop()

        if len(self.stacks[stack_index]) == 0:
            self.open_stacks.pop()

        return value

    def pop_index(self, index):
        return self.stacks[index].pop()
