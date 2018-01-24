def pallendrom(input):
    characters = {}
    num_unique_chars = 0

    for c in input:
        characters[c] = characters.get(c, 0) + 1

    for key in characters:
        if key != " " and characters[key] % 2 != 0:
            num_unique_chars += 1

    return num_unique_chars <= 1

if __name__ == "__main__":
    print(pallendrom("tact coa"))
