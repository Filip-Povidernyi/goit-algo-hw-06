from collections import deque


def bfs_path(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path

        visited.add(current)
        for neighbor in graph.successors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None


def dfs_path(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()

    visited.add(start)
    if start == goal:
        return path

    for neighbor in graph.successors(start):
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, goal,
                                path + [neighbor], visited)
            if new_path:
                return new_path
    return None
