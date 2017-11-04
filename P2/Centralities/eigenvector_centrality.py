import networkx as nx

G = nx.read_edgelist("edges.txt", delimiter=",")

evc = nx.eigenvector_centrality_numpy(G)

evc_values = sorted(evc.values(), reverse = True)

#selects top 3 nodes with highest values
top3 = evc_values[0:3]

print("Top 3 nodes with maximum values")
for node,evcen in evc.items():
    for i in top3:
        if i == evcen:
          print("For node \t" + str(node) + "\tEigenvector centrality Value is \t" + str(i))
