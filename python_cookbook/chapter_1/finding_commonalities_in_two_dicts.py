def run():
    a = dict(
        x=1,
        y=2,
        z=3
    )

    b = dict(
        w=10,
        x=11,
        y=2
    )

    print("Finding keys in common")
    print(a.keys() & b.keys())

    print("Find keys in a that are not in b")
    print(a.keys() - b.keys())

    print("Find (key, value) pairs in common")
    print(a.items() & b.items())

    print("Make a new dict with certain keys removed")
    print({key:a[key] for key in a.keys() - {'z', 'w'}})

if __name__ == '__main__':
    """
    Problem: You have two dictionaries and want to
    find out what they might have in common.
    
    Notes: The keys() method of a dict returns a keys-view object that
    exposes the keys. They also support unions, intersections,
    and differences.
    """
    run()
