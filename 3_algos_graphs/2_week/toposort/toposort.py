#Uses python3

import sys

def dfs(adj):
    visited = [False for _ in range(n)]
    order = []
    def Explore(i):
        visited[i] = True
        for j in adj[i]:
            if visited[j]:
                continue
            else:
                Explore(j)
        order.insert(0, i)
    for v in range(n):
        if not visited[v]:
            Explore(v)
    return order

def toposort(adj):
    order = dfs(adj)
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

