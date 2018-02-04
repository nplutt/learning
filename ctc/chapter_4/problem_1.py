def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def paths_exist(graph, start, end):
    return len(list(bfs_paths(graph, start, end))) > 0

if __name__ == '__main__':
    graph = {'A': ['B', 'C'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F'],
             'D': ['B'],
             'E': ['B', 'F'],
             'F': ['C', 'E']}

    print(paths_exist(graph, 'A', 'B'))

