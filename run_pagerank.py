import argparse
from pagerank.io_utils import read_dat_file
from pagerank.core import pagerank, multiply_Ax
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to Hollins.dat")
    parser.add_argument("--damping", type=float, default=0.15)
    parser.add_argument("--tol", type=float, default=1e-10)
    parser.add_argument("--max-iter", type=int, default=100)
    args = parser.parse_args()

    graph = read_dat_file(args.input)
    ranks = pagerank(graph, damping=args.damping, tol=args.tol, max_iter=args.max_iter)

    # print result
    
    for i, r in enumerate(ranks):
        print(i, r)
    
    print(ranks.sum())
    

if __name__ == "__main__":
    main()