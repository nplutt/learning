def run():
    prices = {
        'ACME': 45,
        'APPL': 612,
        'IBM': 205,
        'HPQ': 37,
        'FB': 10
    }

    # Make a dict of all prices over 200
    p1 = {key: value for key, value in prices.items() if value > 200}
    print(p1)

    # Make a dict of all tech stocks
    tech_names = {'ACME', 'APPL', 'IBM', 'HPQ', 'FB'}
    p2 = {key: value for key, value in prices.items() if key in tech_names}
    print(p2)

if __name__ == '__main__':
    """
    Problem: You want to make a dict into a subset of 
    another dict
    
    Notes: 
    """
    run()
