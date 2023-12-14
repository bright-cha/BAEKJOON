from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    global max_v
    q = deque([])
    for x, y in virus:
        matrix[x][y] = 2
        q.append((x, y))
    while q:
        i, j = q.popleft()

        nx, ny = i + 1, j
        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
            matrix[nx][ny] = 2
            q.append((nx, ny))

        nx, ny = i, j + 1
        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
            matrix[nx][ny] = 2
            q.append((nx, ny))

        nx, ny = i - 1, j
        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
            matrix[nx][ny] = 2
            q.append((nx, ny))

        nx, ny = i, j - 1
        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
            matrix[nx][ny] = 2
            q.append((nx, ny))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                cnt += 1
            if matrix[i][j] == 2:
                matrix[i][j] = 0

    max_v = max(max_v, cnt)


def combination(idx, lst):
    if len(lst) > 3:
        return

    if idx == len(road):
        if len(lst) == 3:
            for x, y in lst:
                matrix[x][y] = 1
            bfs()
            for x, y in lst:
                matrix[x][y] = 0
        return

    else:
        combination(idx + 1, lst + [road[idx]])
        combination(idx + 1, lst)


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

road = []
virus = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            road.append((i, j))
        if matrix[i][j] == 2:
            virus.append((i, j))

max_v = 0
combination(0, [])

print(max_v)