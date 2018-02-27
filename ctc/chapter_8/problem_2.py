def get_p(maze):
    if maze is None or len(maze) == 0:
        return None

    path = []
    failed_points = []

    if get_path(maze, len(maze) -1, len(maze[0]) - 1, path, failed_points):
        return path

    return None


def get_path(maze, row, col, path, failed_paths):
    if row < 0 or col < 0 or row > len(maze) - 1 or col > len(maze[0]) - 1:
        return False

    p = dict(row=row, col=col)

    if p in failed_paths:
        return False

    at_origin = row == 0 and col == 0

    if at_origin or get_path(maze, row-1, col, path, failed_paths) or get_path(maze, row, col-1, failed_paths):
        path.add(p)
        return True

    failed_paths.append(p)
    return False
