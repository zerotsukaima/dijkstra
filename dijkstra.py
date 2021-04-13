inf = float('inf')
start = 0
def dijkstra(G, s):
    n = len(G)
    Q = [(0, s)]
    d = [inf for i in range(n)]
    d[s] = 0
    while len(Q) != 0:
        (cost, u) = Q.pop(0)
        for v in range(n):
            if d[v] > d[u] + G[u][v]:
                d[v] = d[u] + G[u][v]
                Q.append((d[v], v))
    return d

def getPath(f):
    global d
    n = len(G)
    path = [f]
    while f != start:
        for v in range(n):
            if d[v] == d[f] - G[f][v]:
                path.append(v)
                f = v
    return path[::-1]

G = [\
    [inf, 7.0, 9.0, inf, 14.0, inf],\
    [7.0, inf, 10.0, 15.0, inf, inf],\
    [9.0, 10.0, inf, 11.0, 2.0, inf],\
    [inf, 15.0, 11.0, inf, 6.0, inf],\
    [14.0, inf, 2.0, 6.0, inf, 9.0],\
    [inf, inf, inf, inf, 9.0, inf]]

d = dijkstra(G, start)
print(d)
print(getPath(3))