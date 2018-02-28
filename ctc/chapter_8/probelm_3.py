def find_magic_index(arr):
    for i, value in enumerate(arr):
        if i == value:
            return i
    return None


def find_magic_index_recursive(arr, start=None, end=None):
    if start is None:
        start = 0

    if end is None:
        end = len(arr) - 1

    mid = (end - start) / 2 + start

    if end - start <= 1 and mid != arr[mid]:
        return None

    if arr[mid] < mid:
        return find_magic_index_recursive(arr, mid+1, end)
    elif arr[mid] > mid:
        return find_magic_index_recursive(arr, mid-1, end)
    else:
        return mid


if __name__ == "__main__":
    valid_arr = [-10, -1, 0, 1, 2, 4, 5, 7, 10]

    assert find_magic_index(valid_arr) == find_magic_index_recursive(valid_arr) == 7
