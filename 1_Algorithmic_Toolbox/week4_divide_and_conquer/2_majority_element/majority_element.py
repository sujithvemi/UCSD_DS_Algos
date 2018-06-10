# Uses python3
import sys
import math

def get_count(a, elem):
    count = 0
    for i in range(len(a)):
        if a[i] == elem:
            count += 1
    return count

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    mid = math.floor((left+right)/2)
    left_sub = a[:mid]
    right_sub = a[mid:]
    major_left = get_majority_element(a, 0, mid)
    major_right = get_majority_element(a, mid, right)
    if major_left == -1 and major_right != -1:
        right_count = get_count(right_sub, major_right)
        if right_count > len(right_sub)/2:
            return major_right
        else:
            return -1
    elif major_left != -1 and major_right == -1:
        left_count = get_count(left_sub, major_left)
        if left_count > len(left_sub)/2:
            return major_left
        else:
            return -1
    elif major_left != -1 and major_right != -1:
        left_count = get_count(left_sub, major_left)
        right_count = get_count(right_sub, major_right)
        if left_count > len(left_sub)/2:
            return major_left
        elif right_count > len(right_sub)/2:
            return major_right
        else:
            return -1
    else:
        return -1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
