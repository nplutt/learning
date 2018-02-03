from decimal import Decimal


def rounding_numeric_values():
    print(rounding_numeric_values.__name__)

    print(round(1.23, 1))
    print(round(1.235, 2))

    print(format(1.23456, '0.2f'))


def performing_decimal_calculations():
    print(performing_decimal_calculations.__name__)

    a = 4.2
    b = 3.1
    print(a + b)

    # Decimals have much slower performance than floats
    c = Decimal('4.2')
    d = Decimal('3.1')
    print(c + d)

if __name__ == '__main__':
    rounding_numeric_values()
    performing_decimal_calculations()
