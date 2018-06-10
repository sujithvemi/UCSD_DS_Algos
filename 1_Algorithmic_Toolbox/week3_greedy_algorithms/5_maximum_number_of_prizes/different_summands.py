# Uses python3
import sys

def optimal_summands(n):
    summands = []
    prizes = 1
    sum_value = prizes
    summands.append(prizes)
    while sum_value < n:
        prizes += 1
        if sum_value + prizes > n:
            summands[-1] += n - sum_value
            sum_value = n
        else:
            summands.append(prizes)
            sum_value += prizes
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
