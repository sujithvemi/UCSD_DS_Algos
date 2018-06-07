#Uses python3
import sys
import math

def is_greater_equal(digit, max_digit):
    comparison = True
    
def largest_number(a):
    res = ""
    while a:
        max_digit = -math.inf
        for digit in a:
            if is_greater_equal(digit, max_digit):
                max_digit = digit
        res += max_digit
        a.remove(max_digit)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
