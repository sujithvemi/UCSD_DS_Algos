#Uses python3

import sys
import queue
import math

class Node:
    def __init__(self, v_num, dist):
        self.num = v_num
        self.dist = dist

class make_queue:
    def __init__(self, n):
        min_heap = [[] for _ in range(n)]
        size = -1

    def append(self, node):
        self.size += 1
        self.min_heap[self.size] = node

    def left_child(self, i):
        return (2*i + 1)

    def right_child(self, i):
        return (2*i + 2)

    def parent(self, i):
        return math.floor((i-1)/2)

    def sift_up(self, i):
        min_id = parent(i)
        if min_id != -1 and self.min_heap[min_id]['dist'] > self.min_heap[i]['dist']:
            self.min_heap[i], self.min_heap[min_id] = self.min_heap[min_id], self.min_heap[i]
            self.sift_up(min_id)
        else:
            return

    def sift_down(self, i):
        min_id = i
        l_child = left_child(i)
        if l_child <= self.size and self.min_heap[l_child] < self.min_heap[min_id]:
            min_id = l_child
        r_child = right_child(i)
        if r_child <= self.size and self.min_heap[r_child] < self.min_heap[min_id]:
            min_id = r_child
        if min_id != i:
            self.min_heap[min_id], self.min_heap[i] = self.min_heap[i], self.min_heap[min_id]
        else:
            return

    def extract_min(self):
        min_val = self.min_heap[0]
        self.min_heap[0] = self.min_heap[self.size]
        self.size -= 1
        self.sift_down(0)
        return min_val

    def change_priority(self, i, dist):
        old_p = self.min_heap[i]['dist']
        self.min_heap[i]['dist'] = dist
        if dist < old_p:
            self.sift_up(i)
        else:
            self.sift_down(i)

def distance(adj, cost, s, t):
    dist = [float("inf") for _ in range(n)]
    prev = [None for _ in range(n)]
    v_queue = make_queue()
    for i in range(n):
        v_queue.append(Node(i, float("inf")))
           

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
