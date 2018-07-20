#Uses python3

import sys
import queue
import math

class Node:
    def __init__(self, v_num, dist):
        self.num = v_num
        self.dist = dist

class make_queue:
    def __init__(self):
        # self.min_heap = [[] for _ in range(n)]
        self.min_heap = []
        self.size = -1
        self.pos_array = []

    def append(self, node):
        self.size += 1
        self.min_heap.append(node)
        self.pos_array
        self.pos_array.append(self.size)

    def left_child(self, i):
        return (2*i + 1)

    def right_child(self, i):
        return (2*i + 2)

    def parent(self, i):
        return math.floor((i-1)/2)

    def sift_up(self, i):
        min_id = self.parent(i)
        if min_id != -1 and self.min_heap[min_id].dist > self.min_heap[i].dist:
            self.pos_array[self.min_heap[i].num] = min_id
            self.pos_array[self.min_heap[min_id].num] = i
            self.min_heap[i], self.min_heap[min_id] = self.min_heap[min_id], self.min_heap[i]
            self.sift_up(min_id)
        else:
            return

    def sift_down(self, i):
        min_id = i
        l_child = self.left_child(i)
        if l_child <= self.size and self.min_heap[l_child].dist < self.min_heap[min_id].dist:
            min_id = l_child
        r_child = self.right_child(i)
        if r_child <= self.size and self.min_heap[r_child].dist < self.min_heap[min_id].dist:
            min_id = r_child
        if min_id != i:
            self.pos_array[self.min_heap[i].num] = min_id
            self.pos_array[self.min_heap[min_id].num] = i
            self.min_heap[min_id], self.min_heap[i] = self.min_heap[i], self.min_heap[min_id]
        else:
            return

    def extract_min(self):
        min_val = self.min_heap[0]
        last_node = self.min_heap.pop()
        if self.min_heap:
            self.min_heap[0] = last_node
        self.pos_array[last_node.num] = 0
        self.size -= 1
        self.sift_down(0)
        return min_val
    
    def change_priority(self, i, dist):
        pos = self.pos_array[i]
        old_p = self.min_heap[pos].dist
        self.min_heap[pos].dist = dist
        if old_p > dist:
            self.sift_up(pos)
        else:
            self.sift_down(pos)

def distance(adj, cost, s):
    dist = [float("inf") for _ in range(n)]
    prev = [None for _ in range(n)]
    v_queue = make_queue()
    visited = [False for _ in range(n)]
    dist_vals = [float("inf") for _ in range(n)]
    for i in range(n):
        v_queue.append(Node(i, float("inf")))
    v_queue.change_priority(s, 0)
    dist_vals[s] = 0
    while v_queue.min_heap:
        u = v_queue.extract_min()
        visited[u.num] = True
        for v, w in zip(adj[u.num], cost[u.num]):
            if dist_vals[v] > dist_vals[u.num] + w:
                dist_vals[v] = dist_vals[u.num] + w
                prev[v] = u.num
                v_queue.change_priority(v, dist_vals[v])
    del dist_vals[s]
    return [-1 if math.isinf(u) else u for u in dist_vals]

if __name__ == '__main__':
    t = input()
    for i in range(int(t)):
        n, m = input().split()
        n = int(n)
        m = int(m)
        data = []
        for _ in range(m + 1):
            data.extend(list(map(int, input().split())))
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[] for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1].append(w)
            adj[b-1].append(a-1)
            cost[b-1].append(w)
        s = data[0] - 1
        if i == 1:
            for a, b in zip(adj[59], cost[59]):
                print(59, a, b)
            for a, b in zip(adj[2], cost[2]):
                print(2, a, b)
        # print(*distance(adj, cost, s))
        distance(adj, cost, s)
