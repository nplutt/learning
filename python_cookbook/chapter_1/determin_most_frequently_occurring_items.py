from collections import Counter


def run():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]

    word_counts = Counter(words)
    top_three = word_counts.most_common(3)
    print("Top three most common words")
    print(top_three)

    print("Number of times eyes occurs")
    print(word_counts['eyes'])

    print("Counters can be combined")
    word_counts_2 = Counter(words)
    total = word_counts + word_counts_2
    print(total['eyes'])


if __name__ == '__main__':
    """
    Problem: Have a sequence of items and you want to determine the 
    most frequently occurring items.
    
    Notes: Counter objects can be fed any sequence og hashable input 
    items. Counter is a dictionary that maps the items to the number
    of occurrences. Counter objects can be added and subtracted as well.
    """
    run()
