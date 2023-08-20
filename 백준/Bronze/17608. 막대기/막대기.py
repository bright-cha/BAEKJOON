import sys
input = sys.stdin.readline
cnt = int(input())
height = [int(input()) for _ in range(cnt)]
rst = 0
start = 0

for _ in range(cnt):
    value = height.pop()
    if start < value:
        start = value
        rst += 1

print(rst)