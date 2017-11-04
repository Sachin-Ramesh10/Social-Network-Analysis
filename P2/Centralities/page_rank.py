import networkx as nx

G = nx.read_edgelist("edges.txt", delimiter=",")

pr = nx.pagerank(G)

pr_value = sorted(pr.values(), reverse = True)

#selects top 3 nodes with highest values
top3 = pr_value[0:3]

print("Top 3 nodes with maximum values")
for node,page_values in pr.items():
    for i in top3:
        if i == page_values:
          print("For node \t" + str(node) + "\tPage Rank Value is \t" + str(i))
