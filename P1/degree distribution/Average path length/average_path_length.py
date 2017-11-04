from igraph import *

#provided edges.txt file with " " instead of ","
G = Graph.Read_Ncol('edges1.txt', directed=False)

apl = G.average_path_length(directed=False, unconn=True)

print(apl)