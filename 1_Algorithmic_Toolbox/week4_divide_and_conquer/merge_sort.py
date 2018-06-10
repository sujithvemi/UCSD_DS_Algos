#Uses python3
import sys
import math

def merge(b, c):
    d = []
    count = 0
    while b and c:
        if b[0] <= c[0]:
            d.append(b[0])
            b.pop(0)
        else:
            d.append(c[0])
            c.pop(0)
            count += len(b)
    while b:
        d.extend(b)
        b = []
    while c:
        d.extend(c)
        c = []
    return d, count

def merge_sort(a):
    inversions = 0
    if len(a) == 1:
        return a, inversions
    mid = math.floor(len(a)/2)
    b, inv_l = merge_sort(a[:mid])
    c, inv_r = merge_sort(a[mid:])
    a_sort, merge_inv = merge(b, c)
    inversions = inv_l + inv_r + merge_inv
    return a_sort, inversions

if __name__ == "__main__":
    input_vals = sys.stdin.read()
    n, *a = list(map(int, input_vals.split()))
    _, n_inv = merge_sort(a)
    print(n_inv)