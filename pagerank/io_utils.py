from pagerank.graph import Graph

def read_dat_file(path: str) -> Graph:
    """
    Read a .dat file with the following structure:

    Line 1:    n_pages  n_edges
    Next n:    one page label per line
    Next m:    edges: src  dst  (labels, not necessarily 0..n-1)

    Returns a Graph with 0-based internal node indices.
    """
    with open(path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    # --- 1. First line: n_pages, n_edges ---
    first = lines[0].split()
    if len(first) < 2:
        raise ValueError(f"First line must contain at least 2 integers, got: {lines[0]}")
    n = int(first[0])
    m = int(first[1])

    # --- 2. Next n lines: page labels ---
    page_labels = []
    for i in range(1, 1 + n):
        parts = lines[i].split()
        # usually just one label per line
        label = int(parts[0])
        page_labels.append(label)

    # Build mapping from original label -> 0-based index
    label_to_idx = {label: idx for idx, label in enumerate(page_labels)}

    # --- 3. Next m lines: edges (src, dst) using original labels ---
    edges = []
    start = 1 + n
    end = start + m
    for line in lines[start:end]:
        parts = line.split()
        if len(parts) < 2:
            continue  # or raise, depending on how strict you want to be
        src_label = int(parts[0])
        dst_label = int(parts[1])
        # map to 0-based indices
        src = label_to_idx[src_label]
        dst = label_to_idx[dst_label]
        edges.append((src, dst))

    # --- 4. Build Graph with 0-based indices ---
    graph = Graph.from_edge_list(n, edges, zero_based=True)
    return graph
