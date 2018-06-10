# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    unit_val = [v/w for v,w in zip(values, weights)]
    v_sort = [x for _,x in sorted(zip(unit_val, values), reverse=True)]
    w_sort = [x for _,x in sorted(zip(unit_val, weights), reverse=True)]
    for i in range(len(weights)):
        more_loot = min(capacity, w_sort[i])
        value += more_loot * (v_sort[i]/w_sort[i])
        capacity -= more_loot
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
