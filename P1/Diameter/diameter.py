import networkx as nx

G = nx.read_edgelist("edges.txt", delimiter=",")
print("processing")
diameter = nx.diameter(G, e=None)
print(diameter)