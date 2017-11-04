import networkx as nx

G = nx.read_edgelist("edges.txt", delimiter=",")

dc = nx.degree_centrality(G)

dc_values = sorted(dc.values(), reverse = True)

#selects top 3 nodes with highest values
top3 = dc_values[0:3]

print("Top 3 nodes with maximum values")
print(top3)
for node,degcen in dc.items():
    for i in top3:
        if i == degcen:
          print("For node \t" + str(node) + "\t Degree centrality Value is \t" + str(i))
