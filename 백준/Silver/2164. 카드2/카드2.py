from collections import deque

N = deque([i for i in range(1, int(input().strip()) + 1)])
while len(N) != 1:
    N.popleft()
    N.append(N.popleft())

print(*N)