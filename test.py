f = open('zhanna_graph.txt')
G = [line.split() for line in f]
for i in range(len(G)):
    print('')
    for j in range(len(G)):
        print(G[i][j], end=", ")
f.close()