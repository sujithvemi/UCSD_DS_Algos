# Uses python3
import sys

COIN_DENOMS = [1, 3, 4]
def get_change(m):
    min_coin_array = []
    min_coin_array.append(0)
    for i in range(1, m+1):
        min_coins = float("inf")
        for j in COIN_DENOMS:
            if i >= j:
                num_coins = min_coin_array[i - j] + 1
            if num_coins < min_coins:
                min_coins = num_coins
        min_coin_array.append(min_coins)
    return min_coin_array[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
