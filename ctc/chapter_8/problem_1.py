def subset_sum(values, target):
    table = [0 for k in range(target+1)]

    table[0] = 1

    for i in range(len(values)):
        for j in range(values[i], target + 1):
            table[j] += table[j - values[i]]

    return table[target]

if __name__ == '__main__':
    print(subset_sum([1, 2, 3], 10))