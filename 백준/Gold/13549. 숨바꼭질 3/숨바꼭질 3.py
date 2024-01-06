from collections import deque

N, K = map(int, input().split())
max_v = 0
if K > N:
    max_v = (K * 2) + 1
else:
    max_v = (N * 2) + 1

visited = [0] * max_v

q = deque([(N, 0)])
delta = [-1, 1]
x = t = 0
min_v = 1000000
while q:
    x, t = q.popleft()
    if x == K:
        min_v = min(min_v, t)
        break

    if visited[x] == 1 or min_v <= t:
        continue
    visited[x] = 1

    if 0 <= 2 * x < max_v and visited[2 * x] == 0:
        q.append((2 * x, t))

    for i in delta:
        if 0 <= x + i < max_v and visited[x + i] == 0:
            q.append((x + i, t + 1))

print(min_v)