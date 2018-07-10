#Uses python3

import sys

sys.setrecursionlimit(200000)

def Explore(adj, i, visited, *args):
    visited[i] = True
    for j in adj[i]:
        if visited[j] == True:
            continue
        else:
            if args:
                post_order = args[0]
                if post_order is not None:
                    Explore(adj, j, visited, post_order)
            else:
                Explore(adj, j, visited)
    if args:
        post_order = args[0]
        if post_order is not None:
            post_order.append(i)

def dfs(adj):
    visited = [False for _ in range(n)]
    post_order = []
    Explore(adj, 0, visited, post_order)
    return post_order

def number_of_strongly_connected_components(adj):
    result = 0
    visited = [False for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    for i in range(n):
        for target in adj[i]:
            rev_adj[target].append(i)
    post_order = dfs(rev_adj)
    for v in reversed(post_order):
        if not visited[v]:
            result += 1
            Explore(adj, v, visited)
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
