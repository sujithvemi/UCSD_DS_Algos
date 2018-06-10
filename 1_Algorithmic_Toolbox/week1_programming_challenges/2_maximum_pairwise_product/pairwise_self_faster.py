# Uses python3

n = int(input())
a = [int(x) for x in input().split()]

index = 0
for i in range(1, n):
    if a[i] > a[index]:
        index = i
temp = a[n-1]
a[n-1] = a[index]
a[index] = temp

index = 0
for i in range(1, n-1):
    if a[i] > a[index]:
        index = i

temp = a[n-2]
a[n-2] = a[index]
a[index] = temp
print(a[n-2]*a[n-1])