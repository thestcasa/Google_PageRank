from pagerank.graph import Graph
import numpy as np

def multiply_Ax(graph: Graph, x: np.ndarray):

    if len(x) != graph.n:
        raise ValueError(f"x must have length {graph.n}, got {len(x)}")

    n = graph.n
    y = np.zeros(n, dtype=float)

    for src in range(n - 1):
        n_out = graph.out_degree[src]

        # dangling node check
        if n_out == 0:
            continue

        contrib = x[src] / n_out
        out_neigh = graph.out_neighbors[src]

        for n in out_neigh:
            y[n] += contrib

    return y


def pagerank(
        graph: Graph,
        damping: float = 0.15,
        tol: float = 1e-10,
        max_iter: int = 100,
        ) -> np.ndarray:
    
    n = graph.n
    if n == 0:
        return np.array([], dtype=float)
    
    x = np.full(shape=n, fill_value=1/n, dtype=float)

    # all needed constants
    m = damping
    one_minus_m = 1 - m
    inv_n = 1 / n
    out_degree = graph.out_degree

    dangling_mask = np.array([deg == 0 for deg in out_degree])

    # loop
    for _ in range(max_iter):
        Ax = multiply_Ax(graph, x)
        dangling_mass = sum(x[dangling_mask])

        # compute new_x
        new_x = one_minus_m * Ax
        # dangling mass contribution
        new_x += one_minus_m * dangling_mass * inv_n
        # teleportation
        new_x += m * inv_n

        diff = np.abs(new_x - x).sum()

        x = new_x

        if diff < tol:
            break

    s = x.sum()
    if s != 0.0:
        x = x / s
    
    return x