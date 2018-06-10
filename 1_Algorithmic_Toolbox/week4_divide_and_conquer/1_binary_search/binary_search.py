# Uses python3
import sys
import math

def binary_search(a, left, right, x):
    mid = math.floor((left + right)/2)
    if left == right:
        return -1
    if a[mid] == x:
        return mid
    elif a[mid] < x:
        return binary_search(a, mid+1, len(a), x)
    else:
        return binary_search(a, left, mid, x)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, 0, n, x), end = ' ')
