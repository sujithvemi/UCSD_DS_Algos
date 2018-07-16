#Uses python3

import sys
import queue

def bipartite(adj):
    dist = [-1 for _ in range(n)]
    dist[0] = 0
    vert_q = [0]
    is_bipartite = True
    while vert_q:
        u = vert_q.pop(0)
        for v in adj[u]:
            if dist[v] == -1:
                vert_q.append(v)
                dist[v] = dist[u] + 1
            elif dist[v] == dist[u]:
                is_bipartite = False
                break
        if not is_bipartite:
            break
    return int(is_bipartite)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
