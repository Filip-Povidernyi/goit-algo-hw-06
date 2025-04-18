from dfs_bfs import dfs_path, bfs_path
import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()

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

pos = nx.spring_layout(G, seed=42)
edge_labels = nx.get_edge_attributes(G, 'weight')

nx.draw(G, pos, with_labels=True, node_color='skyblue',
        node_size=3500, font_size=9, font_weight='regular', edge_color='yellow')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Граф міст України")
plt.show()


if __name__ == '__main__':

    start_city = "Kyiv"
    end_city = "Zaporizhzhia"

    bfs_result = bfs_path(G, start_city, end_city)
    dfs_result = dfs_path(G, start_city, end_city)

    print("BFS шлях:", bfs_result)
    print("DFS шлях:", dfs_result)
