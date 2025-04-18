import networkx as nx
import matplotlib.pyplot as plt


def main():
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
    nx.draw(G, pos, with_labels=True, node_color='skyblue',
            node_size=3500, font_size=9, font_weight='regular', edge_color='yellow')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(
        u, v): d['weight'] for u, v, d in G.edges(data=True)}, font_size=10)
    plt.title("Мережа міст")
    plt.show()

    print("Кількість вершин (міст):", G.number_of_nodes())
    print("Кількість ребер (доріг):", G.number_of_edges())

    print("\nСтупінь вершин:")
    for city in G.nodes():
        print(f"{city}: вхідний — {G.in_degree(city)}, вихідний — {G.out_degree(city)}")


if __name__ == '__main__':
    main()
