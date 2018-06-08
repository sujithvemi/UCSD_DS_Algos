# Uses python3
import sys

OPS = ["1", "2", "3"]
def optimal_dynamic(n):
    build_seq = []
    build_seq.append([1])
    num_ops = []
    num_ops.append(0)
    for i in range(2, n + 1):
        min_ops = float("inf")
        for op in OPS:
            if op == "1" and i % 3 == 0:
                ops_req = num_ops[int((i/3)) - 1] + 1
                if ops_req < min_ops:
                    min_ops = ops_req
                    min_sequence = list(build_seq[int((i/3)) - 1])
                    min_sequence.append(i)
            elif op == "2" and i % 2 == 0:
                ops_req = num_ops[int((i/2)) - 1] + 1
                if ops_req < min_ops:
                    min_ops = ops_req
                    min_sequence = list(build_seq[int((i/2)) - 1])
                    min_sequence.append(i)
            elif op == "3":
                ops_req = num_ops[i - 2] + 1
                if ops_req < min_ops:
                    min_ops = ops_req
                    min_sequence = list(build_seq[i - 2])
                    min_sequence.append(i)
        build_seq.append(min_sequence)
        num_ops.append(min_ops)
    return build_seq[n - 1]

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_dynamic(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
