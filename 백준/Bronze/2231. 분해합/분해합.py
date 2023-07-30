import sys
input = sys.stdin.readline

n = int(input())

res = []
for i in range(n):
    sum_num = 0
    for j in str(i):
        sum_num += int(j)
    if i + sum_num == n:
        res.append(i)

if res == []:
    print(0)
else:
    print(min(res))