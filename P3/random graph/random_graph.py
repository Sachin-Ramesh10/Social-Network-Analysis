import networkx as nx
import math
import matplotlib.pyplot as plt

def avg_degree(A):
    degree = A.degree()
    Average_degree = sum(degree.values())/float(len(A))
    return Average_degree

S = nx.Graph()
G = nx.read_edgelist("edges.txt", delimiter=",")
k = avg_degree(G)
print("The average degree of original graph is \t",k)

#propabilty of edge creation
p = k/(G.number_of_nodes() - 1)

S.add_edges_from((nx.fast_gnp_random_graph(G.number_of_nodes(), p, seed=None, directed=False)).edges())
c = avg_degree(S)

avg_clusco = nx.average_clustering(S)
print("Average local Clustering\t" + str(avg_clusco))

#average path length
apl = math.log(S.number_of_nodes())/float(math.log(c))

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
plt.title ("Degree Distribution of random graph")
fig.savefig ("degree_distribution_randomg1.png")
fig.show()