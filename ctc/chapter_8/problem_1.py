def subset_sum(values, target):
    table = [0 for k in range(target+1)]
    table[0] = 1
    for i in range(len(values)):
        for j in range(values[i], target + 1):
            table[j] += table[j - values[i]]

    return table[target]


def sums(values, value):
    if type(values) is not list:
        raise ValueError
    elif type(value) is not int:
        raise ValueError

    arr = [[1 for i in range(value + 1)] for j in enumerate(values)]

    for r, v in enumerate(values):
        for c in range(0, value + 1):
            if c > 0:
                if c - v >= 0:
                    previous = arr[r][c - v]
                else:
                    previous = 0

                if r - 1 >= 0:
                    upper = arr[r-1][c]
                else:
                    upper = 0
                arr[r][c] = upper + previous

    return arr[len(values) - 1][value]


if __name__ == '__main__':
    print(subset_sum([1, 2, 3], 3))
    print(sums([1, 2, 3], 3))

    print(subset_sum([1, 2, 3], 5))
    print(sums([1, 2, 3], 5))

    print(subset_sum([1, 2, 3], 6))
    print(sums([1, 2, 3], 6))