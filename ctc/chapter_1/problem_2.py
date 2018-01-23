def permutation(base_str, perm_str):
    base_arr = [0] * 128

    for c in base_str:
        base_arr[ord(c)] += 1

    for c in perm_str:
        base_arr[ord(c)] -= 1

        if base_arr[ord(c)] < 0:
            return False

    return True


if __name__ == "__main__":
    print(permutation("hello world", "dohllll"))
