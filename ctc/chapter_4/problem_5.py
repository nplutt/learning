def valid_bst(start, min=None, max=None):
    if start is None:
        return None

    if (min is not None and start.val <= min) \
            or (max is not None and start.val >= max):
        return False

    if not valid_bst(start.left, min, start.val) or \
            not valid_bst(start.right, start.val, max):
        return False

    return True
