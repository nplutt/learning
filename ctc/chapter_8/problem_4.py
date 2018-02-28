from copy import deepcopy


def get_subsets(set_values):
    sub_sets = list()
    sub_sets.append([])

    for v in set_values:
        sub_sets_len = len(sub_sets)
        for i in range(0, sub_sets_len):
            sub_copy = deepcopy(sub_sets[i])
            sub_copy.append(v)
            if len(sub_copy) < len(set_values):
                sub_sets.append(sub_copy)

    return sub_sets

if __name__ == "__main__":
    print(get_subsets([1, 2, 3, 4]))
