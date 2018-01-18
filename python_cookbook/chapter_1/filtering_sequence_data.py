def run():
    my_list = [1, 4, -5, 10, -7, 2, 3, -1]

    print([n for n in my_list if n > 0])
    print([n for n in my_list if n < 0])

    pos = (n for n in my_list if n > 0)
    print(pos)

    for x in pos:
        print(x)

    def is_int(val):
        try:
            x = int(val)
            return True
        except ValueError:
            return False

    values = ['1', '2', '-3', '-', '4', 'N/A', '5']

    print(list(filter(is_int, values)))


if __name__ == '__main__':
    """
    Problem: You have data in a sequence and want to 
    extract values or reduce it.
    
    Notes: 
    """
    run()
