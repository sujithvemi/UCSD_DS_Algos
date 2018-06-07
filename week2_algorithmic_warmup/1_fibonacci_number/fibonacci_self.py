# Uses python3
num_1 = 0
num_2 = 1
n = int(input())
for i in range(2, n+1):
    new_num = num_1 + num_2
    num_1 = num_2
    num_2 = new_num
if n == 0 or n == 1:
    print(n)
else:
    print(new_num)