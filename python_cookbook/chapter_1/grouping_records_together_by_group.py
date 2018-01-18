from operator import itemgetter
from itertools import groupby
from collections import defaultdict


def run():
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]

    # Sort by the desired field first
    rows.sort(key=itemgetter('date'))

    # Iterate in groups
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print('    ', i)

    # Using default dict for larger data sets
    rows_by_date = defaultdict(list)
    for row in rows:
        rows_by_date[row['date']].append(row)

    for r in rows_by_date['07/01/2012']:
        print(r)

if __name__ == '__main__':
    """
    Problem: You have a sequence of dicts or instances and you want
    to iterate over the data in groups based on the value of a 
    particular field such as date.
    
    Notes: The groupby() function works by scanning a sequence and 
    finding sequential runs of identical values. On each iteration it 
    returns the value along with an iterator that produces all of the
    items in a group with the same value. Need to sort first because
    groupby() only examines consecutive items. 
    """
    run()
