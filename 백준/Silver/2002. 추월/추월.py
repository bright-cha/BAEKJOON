N = int(input())

start = [input() for _ in range(N)]
end = [input() for _ in range(N)]

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