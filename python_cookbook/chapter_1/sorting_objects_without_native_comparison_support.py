from operator import attrgetter


def run():
    class User:
        def __init__(self, user_id):
            self.user_id = user_id

        def __repr__(self):
            return 'User({})'.format(self.user_id)

    users = [User(23), User(3), User(99)]
    sorted_users = sorted(users, key=lambda u: u.user_id)
    print(sorted_users)

    alt_sorted_users = sorted(users, key=attrgetter('user_id'))
    print(alt_sorted_users)

if __name__ == '__main__':
    """
    Problem: You want to sort objects of the same class, but 
    they don't natively support comparison.
    
    Notes: Either lambda or attrgetter can be used, however 
    attrgetter is usually a bit faster and allows multiple keys
    to be fetched. This solution works with min() max() functions.
    """
    run()
