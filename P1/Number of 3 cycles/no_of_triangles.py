import networkx as nx

G = nx.read_edgelist("edges.txt", delimiter=",")

triangles = sum(list(nx.triangles(G).values()))
print("number of triangles\t" + str(triangles))
