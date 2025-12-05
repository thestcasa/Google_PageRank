import pandas as pd


def read_dat_file():
    df = pd.read_csv("/Users/gabrieleadorni/VSC_destination/Google_PageRank/data/hollins.dat", header=None)
    m, n = df.first()
    df_links = 0
    df_edges = 0
    
    return df_links, df_edges