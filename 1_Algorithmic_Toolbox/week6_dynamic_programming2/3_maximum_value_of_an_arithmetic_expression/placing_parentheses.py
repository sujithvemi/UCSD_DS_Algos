# Uses python3

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def find_min_max(i, j, dataset, min_arr, max_arr):
    min_val = float("inf")
    max_val = -float("inf")
    for k in range(i, j):
        op = dataset[k*2+1]
        a = evalt(max_arr[i][k], max_arr[k+1][j], op)
        b = evalt(max_arr[i][k], min_arr[k+1][j], op)
        c = evalt(min_arr[i][k], min_arr[k+1][j], op)
        d = evalt(min_arr[i][k], max_arr[k+1][j], op)
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val

def get_maximum_value(dataset):
    num_digits = int(len(dataset)/2) + 1
    min_arr = [[0]*num_digits for i in range(num_digits)]
    max_arr = [[0]*num_digits for i in range(num_digits)]
    for i in range(num_digits):
        min_arr[i][i] = max_arr[i][i] = int(dataset[2*i])
    for s in range(num_digits):
        for i in range(num_digits - s - 1):
            j = i + s + 1
            min_arr[i][j], max_arr[i][j] = find_min_max(i, j, dataset, min_arr, max_arr)
    return max_arr[0][num_digits - 1]

if __name__ == "__main__":
    print(get_maximum_value(input()))
