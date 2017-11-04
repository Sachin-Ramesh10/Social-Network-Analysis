import networkx as nx
import matplotlib.pyplot as plt


G = nx.read_edgelist("edges.txt", delimiter=",")
degs = {}
for n in G.nodes():
        deg = G.degree(n)
        if deg not in degs:
            degs[deg] = 0
        degs[deg] += 1
items = sorted(degs.items())
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([(k,2) for (k , v ) in items ] , [ (v,2) for (k ,v ) in items])
ax.set_xscale('log')
ax.set_yscale('log')
plt.title ("Degree Distribution")
fig.savefig ("degree_distribution.png")
fig.show()

#calculates y intercept for given values
while(1):
    x1,y1 = items[45]
    x2,y2 = items[70]
    slope =(abs(y2-y1)/float(x2-x1))
    y = (-1 * x1) * slope + y1
    print("Power law intercept \t " + str(y))
    break



