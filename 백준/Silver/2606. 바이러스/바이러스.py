from collections import deque
import sys
input = sys.stdin.readline

def bfs(num):
    q = deque([1])
    visited = [0] * (cnt_cum + 1)
    visited[1] = 1
    cnt = 0
    while q:
        num = q.popleft()
        for i in matrix[num]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1
                q.append(i)
    return cnt


cnt_cum = int(input())
E = int(input())

matrix = [[] for _ in range(cnt_cum + 1)]
for _ in range(E):
    i, j = map(int, input().split())
    matrix[i].append(j)
    matrix[j].append(i)

print(bfs(1))
