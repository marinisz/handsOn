import networkx as nx
import matplotlib.pyplot as plt

graph=nx.Graph()
graph.add_edge(1,2)
graph.add_edge(1,5)
graph.add_edge(2,5)
graph.add_edge(2,3)
graph.add_edge(5,4)
graph.add_edge(4,3)
graph.add_edge(4,6)

clustering_coefficients = nx.clustering(graph)

# calculate degree distribution of each node
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