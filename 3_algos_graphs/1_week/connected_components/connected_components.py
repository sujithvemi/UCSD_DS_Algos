#Uses python3

import sys


def number_of_components(adj):
    result = 0
    visited = [False for _ in range(n)]
    cc_num_arr = [0 for _ in range(n)]
    def Explore(i, cc):
        visited[i] = True
        cc_num_arr[i] = cc
        for j in adj[i]:
            if visited[j]:
                continue
            else:
                Explore(j, cc)
    for v in range(n):
        if not visited[v]:
            result += 1
            Explore(v, result)
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
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
