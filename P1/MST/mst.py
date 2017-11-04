import networkx as nx

weight = []
G = nx.read_edgelist("edges.txt", delimiter=",")

MST = nx.Graph()
W = nx.Graph()
edges = G.edges()

#assigns weights to the existing edges
for edge in edges:
    a,b = edge
    d = abs(G.degree(a) - G.degree(b))
    W.add_edge(a, b, weight=d)

MST = nx.minimum_spanning_tree(W)

diameter = nx.diameter(MST, e=None)

print("diameter is\t " + str(diameter))

#saves the edges with the weights
fh=open("MST_edgelist.txt",'wb')
nx.write_weighted_edgelist(MST, fh)

for (u,v,d) in MST.edges(data=True):
    weight.append(d['weight'])

print("Total Weight of minimum spanning tree is \t" + str(sum(weight)))
