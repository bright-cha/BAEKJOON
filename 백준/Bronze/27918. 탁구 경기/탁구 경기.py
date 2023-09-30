import sys
input = sys.stdin.readline

N = int(input())
rst = [0, 0]
for _ in range(N):
    i = input().rstrip()
    if i == 'D':
        rst[0] += 1
    else:
        rst[1] += 1
    if abs(rst[0] - rst[1]) == 2:
        break

print(':'.join(map(str, rst)))