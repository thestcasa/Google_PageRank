from pagerank.graph import Graph

edges = [(0, 1), (1, 2), (2, 0)]
g = Graph.from_edge_list(3, edges, zero_based=True)
print(g.out_neighbors)   # expect [[1], [2], [0]]
print(g.out_degree)  

