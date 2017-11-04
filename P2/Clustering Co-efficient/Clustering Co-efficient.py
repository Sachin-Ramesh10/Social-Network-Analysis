import networkx as nx

G = nx.read_edgelist("edges.txt", delimiter=",")
local_clusco = nx.average_clustering(G)
print("Average local Clustering\t" + str(local_clusco))

triangles = sum(list(nx.triangles(G).values()))
print("number of triangles\t" + str(triangles))

#searches for nodes with transitive property
def degree_iter(G, nodes=None):
    if nodes is None:
        nodes_nbrs = G.adj.items()
    else:
        nodes_nbrs = ((n, G[n]) for n in G.nbunch_iter(nodes))

    for v, v_nbrs in nodes_nbrs:
        vs = set(v_nbrs) - set([v])
        yield (v, len(vs))

#returns the triples
def triads(G):
    contri = 0
    for v, d in degree_iter(G):
        contri += d * (d - 1)
    return float(contri)


triples = triads(G)

print("Number of Triples\t" + str(triples))

global_clusco = float(triangles * 3) / float(triples)

print("global clustering co-efficient\t" + str(global_clusco))


