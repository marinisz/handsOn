
import matplotlib.pyplot as plt
import networkx as nx

edges_list = []
with open('bio-CE-CX.edges', 'r') as f:
    for line in f:
        nodes = line.strip().split(' ')
        edges_list.append((int(nodes[0]), int(nodes[1])))

graph = nx.Graph()
graph.add_edges_from(edges_list)

clustering_coefficients = nx.clustering(graph)
degrees = dict(graph.degree())

for node in graph.nodes():
    print(f"Node {node}: Clustering coefficient={clustering_coefficients[node]}, Degree={degrees[node]}")
    
print("Number of nodes: ",nx.number_of_nodes(graph))
print("Number of edges: ",nx.number_of_edges(graph))
print("Average degree connectivity: ",nx.average_degree_connectivity(graph))

pos = nx.spring_layout(graph)

nx.draw_networkx(graph, pos, with_labels=True)
plt.show()
degree_dist = nx.degree_histogram(graph)
print("Degree distribution", degree_dist)

components = nx.connected_components(graph)
for i, component in enumerate(components):
    print("Component {}: {}".format(i+1, component))

print("Diameter: ", nx.diameter(graph))

centrality = nx.betweenness_centrality(graph)
for node, cent in centrality.items():
    print("Betweenness centrality of node {}: {}".format(node, cent))
