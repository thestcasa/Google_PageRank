
class Graph:

    def __init__(self, n, out_neighbors):
        if len(out_neighbors) != n:
            raise ValueError("out_neighbors must contain n (number of nodes) elements")
        
        self.n = n
        self.out_neighbors = out_neighbors
        self.out_degree = [len(neigh_list) for neigh_list in out_neighbors]
        pass


    @classmethod
    def from_edge_list(cls, n, edges, zero_based=True):
        """
        Build a Graph from a list of directed edges.

        edges: iterable of pairs (src, dst)
               meaning src -> dst
        """
        out_neighbors = [[] for _ in range(n)]

        for (src, dst) in edges:
            if not zero_based:
                src -= 1
                dst -= 1

            if not (0 <= src < n and 0 <= dst < n):
                raise ValueError(
                    f"Edge ({src}, {dst}) out of range for a graph with {n} nodes"
                )

            out_neighbors[src].append(dst)

        return cls(n, out_neighbors)
        

        

            

