# Uses python3
import sys
import math

def get_change(m):
    coins = 0
    denoms = [10, 5, 1]
    for val in denoms:
        coins_needed = int(math.floor(m/val))
        coins += coins_needed
        m -= coins_needed * val
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
