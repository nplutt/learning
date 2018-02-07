class Junk(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs(start, arr=[], depth=0):
    if start is None:
        return None

    try:
        arr[depth] += 1
    except IndexError:
        arr.append(1)

    depth += 1

    dfs(start.left, arr, depth)
    dfs(start.right, arr, depth)

    return arr


def balanced(root):
    arr = dfs(root)

    for i, a in enumerate(arr):
        if (i < (len(arr) - 2)) and (a * 2 > arr[i + 1]) and ((i + 2) - (len(arr) - 1) >= 0):
            return False

    return True

if __name__ == '__main__':
    root = Junk(1)
    root.left = Junk(2)
    root.left.left = Junk(3)
    root.left.right = Junk(3)
    root.right = Junk(2)
    root.right.left = Junk(3)
    root.right.right = Junk(3)
    root.right.right.right = Junk(4)
    root.right.right.right.right = Junk(5)

    print(balanced(root))

