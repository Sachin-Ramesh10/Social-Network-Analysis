import networkx as nx

G = nx.read_edgelist("edges.txt", delimiter=",")

preds = nx.jaccard_coefficient(G)

for u,v,p in preds:
    with open('Pair_of_Most_SimilarNodes.txt', 'a') as f:
     if p == 1:
      print("\t" + str(u) + "\t" + str(v), file=f)
