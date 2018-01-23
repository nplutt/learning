def unique_string(st):
    if len(st) > 128:
        return False

    char_arr = [False] * 128
    for c in st:
        index = ord(c)
        if not char_arr[index]:
            char_arr[index] = True
        else:
            return False

    return True

if __name__ == "__main__":
    print(unique_string("helo warkd"))
    print(unique_string("hello world!"))
