#Uses python3

import sys


def acyclic(adj):
    visited = [False for _ in range(n)]
    recStack = [False for _ in range(n)]
    def isCyclic(i):
        visited[i] = True
        recStack[i] = True
        for j in adj[i]:
            if not visited[j]:
                if isCyclic(j) == True:
                    return True
            elif recStack[j] == True:
                return True
        recStack[i] = False
        return False
    
    for i in range(n):
        if not visited[i]:
            if isCyclic(i) == True:
                return int(True)
    return int(False)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
