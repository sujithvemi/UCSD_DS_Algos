#Uses python3
import sys
import operator

def max_dot_product(a, b):
    res = 0
    a_sort = sorted(a, reverse=True)
    b_sort = sorted(b, reverse=True)
    multiply = lambda a,b: map(operator.mul, a, b)
    res = sum(multiply(a_sort, b_sort))
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
