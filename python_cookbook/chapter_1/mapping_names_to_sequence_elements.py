from collections import namedtuple


def run():
    Subscriber = namedtuple('Subscriber', ['address', 'joined'])
    sub = Subscriber('Nick', '2012-10-19')
    print(sub)

    print(sub.address)
    print(sub.joined)

    address, joined = sub
    print(address)
    print(joined)


if __name__ == '__main__':
    """
    Problem: You have code that accesses a list or tuple
    elements by position, this makes the code unreadable. Also
    you would like to be less dependent on the structure.
    
    Notes: Using namedtuple() method, which is a factory method
    that returns a subclass of the standard python tuple() type.
    You pass a type name and the fields it should have. This returns 
    a class that you can instantiate by passing values for fields. The
    main use case is to decouple your code from the position of the 
    elements that it manipulates. Another use is in the place of dicts,
    namedtuples are more efficient and take up less space. Beware that
    namedtuples are immutable though. If you goal is to define an 
    efficient data structure you are better off defining a class using
    __slots__ instead. 
    """
    run()
