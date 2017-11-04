import networkx as nx
import math
import matplotlib.pyplot as plt
from igraph import *


def avg_degree(A):
    degree = A.degree()
    Average_degree = sum(degree.values())/float(len(A))
    return Average_degree

S = nx.Graph()
G = nx.read_edgelist("edges.txt", delimiter=",")

print("started")
S.add_edges_from((nx.barabasi_albert_graph(G.number_of_nodes(), 15, seed=None)).edges())

avg_clusco = nx.average_clustering(S)
print("Average local Clustering\t" + str(avg_clusco))

#average path length
apl = math.log(S.number_of_nodes())/float(math.log(math.log(S.number_of_nodes())))

print("Average path length of simulated model \t", apl)

degs = {}
for n in S.nodes():
        deg = S.degree( n )
        if deg not in degs:
            degs[deg] = 0
        degs[deg] += 1
items = sorted(degs.items())
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter([(k,2) for (k , v ) in items ] , [(v,2) for (k ,v ) in items])
ax.set_xscale('log')
ax.set_yscale('log')
plt.title ("Degree Distribution of preferential Attachment graph")
fig.savefig ("degree_distribution_prefatch.png")
fig.show()

