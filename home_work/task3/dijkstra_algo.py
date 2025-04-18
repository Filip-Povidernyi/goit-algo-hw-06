import networkx as nx


G = nx.Graph()

cities = ['Kyiv', 'Lviv', 'Kharkiv', 'Odesa', 'Dnipro', 'Zaporizhzhia']
G.add_nodes_from(cities)

roads = [
    ('Kyiv', 'Lviv', 540),
    ('Kyiv', 'Kharkiv', 480),
    ('Kyiv', 'Odesa', 475),
    ('Lviv', 'Odesa', 790),
    ('Odesa', 'Dnipro', 500),
    ('Dnipro', 'Zaporizhzhia', 85),
    ('Kharkiv', 'Dnipro', 215),
    ('Zaporizhzhia', 'Kyiv', 500)
]
G.add_weighted_edges_from(roads)


def dijkstra(graph, start):

    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph)

    while unvisited:
        cur_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[cur_vertex] == float('infinity'):
            break
        for neighbor in graph[cur_vertex]:
            weight = graph[cur_vertex][neighbor].get(
                'weight', float('infinity'))
            distance = distances[cur_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
        unvisited.remove(cur_vertex)

    return distances


if __name__ == '__main__':

    for city in cities:
        print(f'Накоротші відстані від міста {city}: {dijkstra(G, city)}')
