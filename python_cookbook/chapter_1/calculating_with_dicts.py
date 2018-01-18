def run():
    prices = dict(
        ACME=45.23,
        AAPL=612.78,
        IBM=205.55,
        HPQ=37.20,
        FB=10.75
    )

    min_price = min(zip(prices.values(), prices.keys()))
    print(min_price)

    max_price = max(zip(prices.values(), prices.keys()))
    print(max_price)

    sort_price = sorted(zip(prices.values(), prices.keys()))
    print(sort_price)


if __name__ == '__main__':
    """
    By using zip() to invert the values, it makes it easier to perform
    calculations. Also zip() produces an iterator that can only be consumed
    once. If normal min() max() functions are run on a dict, they are only 
    run on the keys.
    """
    run()
