import sys
input = sys.stdin.readline

n = int(input())

res = []
for i in range((len(str(n)) * 9) + 1):
    if i < n:
        origin = n - i
    
    num = 0
    for j in str(origin):
        num += int(j)
    
    if origin + num == n:
        res.append(origin)

if res == []:
    print(0)
else:
    print(min(res))