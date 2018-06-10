# Uses python3
import sys

def optimal_weight(W, n, w):
    val_arr = []
    val_arr.append([0]*(W + 1))
    for j in range(1, n+1):
        val_arr.append([0])
    for i in range(1, n + 1):
        for weight in range(1, W + 1):
            val_arr[i].append(val_arr[i-1][weight])
            if w[i-1] <= weight:
                value = val_arr[i-1][weight-w[i-1]] + w[i-1]
                if val_arr[i][weight] < value:
                    val_arr[i][weight] = value
    return val_arr[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, n, w))
