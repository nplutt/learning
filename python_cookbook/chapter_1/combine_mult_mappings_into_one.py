from collections import ChainMap


def run():
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}

    # Check a then b for an item
    c = ChainMap(a, b)
    print(c['z'])



if __name__ == '__main__':
    """
    Problem: You have multiple dicts or mappings that you want to
    combine into a single mapping to perform certain operations.
    
    Notes: ChainMap takes multiple mappings and makes them logically
    appear as one. ChainMap simply keeps a list of the underlying mappings
    and redefines common dictionary operations to scan the list.
    """
    run()
