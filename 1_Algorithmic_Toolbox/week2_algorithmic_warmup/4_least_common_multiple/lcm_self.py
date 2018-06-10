# Uses python3
import sys

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):
    if gcd(a, b) == 1:
        return a*b
    else:
        gcd_val = gcd(a, b)
        return gcd_val * lcm(int(a/gcd_val), int(b/gcd_val))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))