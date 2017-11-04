import networkx as nx

#traverses the graph to find the bridge
def bridge_dfs(G,u,v,count,low,pre,bridges):
        count    += 1
        pre[v]  = count
        low[v]  = pre[v]

        for w in nx.neighbors(G,v):
            if (pre[w] == -1):
                bridge_dfs(G,v,w,count,low,pre,bridges)

                low[v] = min(low[v], low[w])
                if (low[w] == pre[w]):
                    bridges.append((v,w))

            elif (w != u):
                low[v] = min(low[v], pre[w])


def get_bridges(G):
    bridges = []
    count = 0
    low = {n: -1 for n in G.nodes()}
    pre = low.copy()

    for n in G.nodes():
        try:
         bridge_dfs(G, n, n, count, low, pre, bridges)
        except(RecursionError):
         pass

    with open('bridges.txt', 'a') as f:
       print(bridges, file=f)

    return len(bridges)

G = nx.read_edgelist("edges.txt", delimiter=",")
number_of_bridges = get_bridges(G)
print("Number of bridges in a graph \t = \t",number_of_bridges)
