import sys
input = sys.stdin.readline

N = int(input())

start = [input().rstrip() for _ in range(N)]
end = [input().rstrip() for _ in range(N)]

cnt = 0
while end:
    car = end.pop(0)
    if car == start[0]:
        start.remove(car)
        continue
    else:
        start.remove(car)
        cnt += 1

print(cnt)