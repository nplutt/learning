from collections import defaultdict


def run_list():
    d = defaultdict(list)
    print(d)

    d['a'].append(1)
    d['a'].append(2)
    d['a'].append(3)

    d['b'].append(4)
    d['b'].append(5)

    print(d)

    result = dict(
        a=[1, 2, 3],
        b=[4, 5]
    )

    print(result)

    assert result == d


def run_set():
    c = defaultdict(set)
    print(c)

    c['a'].add(1)
    c['a'].add(2)
    c['a'].add(3)

    c['b'].add(4)
    c['b'].add(5)

    print(c)

    result = dict(
        a={1, 2, 3},
        b={4, 5}
    )

    print(result)

    assert result == c


def run_default():
    d = {}
    d.setdefault('a', []).append(1)
    d.setdefault('a', []).append(2)
    d.setdefault('c', []).append(3)

    print(d)

if __name__ == '__main__':
    """
    Using defaultdict is useful when you need to initialize the values
    but don't know if they exist
    """
    run_list()
    run_set()
    run_default()
