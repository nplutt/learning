def run_hashable():
    """
    Solution for a list that has hashable attributes
    """
    def dedupe(items):
        seen = set()
        for item in items:
            if item not in seen:
                yield item
                seen.add(item)

    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))


def run_unhashable():
    """
    Solution for a list that has unhashable types
    """
    def dedupe(items, key=None):
        seen = set()
        for item in items:
            val = item if key is None else key(item)
            if val not in seen:
                yield item
                seen.add(val)

    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))


if __name__ == '__main__':
    """
    Problem: You want to remove duplicate values from a
    sequence but preserve the order.
    
    Notes: If all you want to do is eliminate duplicates
    it is often easy to make a set, this approach doesn't 
    preserve any order though. The use of a generator 
    function shows that you might want this function to be 
    extremely general purpose.
    """
    run_hashable()
    run_unhashable()
