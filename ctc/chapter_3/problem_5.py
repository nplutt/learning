def sort_stack(stack):
    temp_stack = []
    stack_max = None
    ordered = False
    count = 0

    while not ordered:
        while len(stack) > count:
            if stack[len(stack) - 1] > stack_max:
                if stack_max is not None:
                    temp_stack.append(stack_max)
                stack_max = stack.pop()
            else:
                temp_stack.append(stack.pop())

        stack.append(stack_max)
        count += 1

        temp_stack_len = len(temp_stack)

        while len(temp_stack) > 0:
            stack.append(temp_stack.pop())

        stack_max = None

        if temp_stack_len == 0:
            ordered = True

    return stack


if __name__ == "__main__":
    a = [4, 7, 2, 4, 3, 9]
    print(sort_stack(a))
