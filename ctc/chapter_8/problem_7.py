def multiply(val_1, val_2, sum=0):
    if val_2 == 0:
        return sum

    sum += val_1
    val_2 -= 1

    return multiply(val_1, val_2, sum)


if __name__ == "__main__":
    print(multiply(3, 4))