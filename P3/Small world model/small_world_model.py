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
k = avg_degree(G)
print("The average degree of original graph is \t",k)

S.add_edges_from((nx.watts_strogatz_graph(G.number_of_nodes(), 4, 0.1, seed=None)).edges())
c = avg_degree(S)
print(c)

#clustering co-effcient
clustco = 3*(c-2)/float(4*(c-1))

print("Average local Clustering\t" + str(clustco))

with open('swmedg.txt', 'w') as f:
    for i,j in S.edges():
        print(str(i)+" " +str(j), file =f )


pl = Graph.Read_Ncol('swmedg.txt', directed=False)

#average path length

apl = pl.average_path_length(directed=False, unconn=True)

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
ax.plot([(k,2) for (k , v ) in items ] , [(v,2) for (k ,v ) in items])
ax.set_xscale('log')
ax.set_yscale('log')
plt.title ("Degree Distribution of Small world model graph")
fig.savefig ("degree_distribution_swm.png")
fig.show()