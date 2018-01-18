def run():
    ######   0123456789012345678901234567890123456789012345678'
    record = '....................100 .......513.25 ..........'

    # Old Code
    cost = int(record[20:23]) * float(record[31:37])
    print(cost)

    # New Code
    SHARES = slice(20, 23)
    PRICE = slice(31, 37)
    cost = int(record[SHARES]) * float(record[PRICE])
    print(cost)


if __name__ == '__main__':
    """
    Problem: Program has become unreadable and you want to
    clean it up.
    
    Notes: This cleans the code up and makes it more clear as
    to what chunk of the data is.
    """
    run()
