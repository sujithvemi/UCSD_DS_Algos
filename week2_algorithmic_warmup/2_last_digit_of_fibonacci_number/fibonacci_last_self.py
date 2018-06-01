# Uses python3
num_1 = num_2 = 1
n = int(input())
for i in range(3, n+1):
    new_num = (num_1 + num_2)%10
    num_1 = num_2
    num_2 = new_num
print(new_num)