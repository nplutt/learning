from operator import itemgetter


def run():
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]

    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))

    print(rows_by_fname)
    print(rows_by_uid)

    rows_by_lfname = sorted(rows, key=itemgetter('fname', 'lname'))
    print(rows_by_lfname)


if __name__ == '__main__':
    """
    Problem: Sort list of dicts according to one or more
    dict values.
    
    Notes: Used sorted() which accepts a key word argument of
    key. This argument is expected to be callable. This solution
    can also be used with min() max() functions as well.
    """
    run()
