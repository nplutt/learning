def edits(input_string_1, input_string_2):
    len_1 = len(input_string_1)
    len_2 = len(input_string_2)
    max_len = max(len_2, len_1) - 1

    different_chars = 0
    for i in range(0, max_len):
        if input_string_1[i] != input_string_2[i]:
            different_chars += 1

            if len_1 < len_2:
                input_string_1 = input_string_1[:i] + " " + input_string_1[i:]
            elif len_2 < len_1:
                input_string_2 = input_string_2[:i] + " " + input_string_2[i:]

    return different_chars < 2

if __name__ == "__main__":
    print(edits("pale", "ple"))
    print(edits("pales", "pale"))
    print(edits("pale", "bale"))
    print(edits("pale", "elpa"))
    print(edits("pale", "bake"))
    print(edits("appple", "aple"))
