from collections import deque


def bfs(x, y, distance):
    visited = [[0] * N for _ in range(N)]
    q = deque([(x, y, distance)])
    visited[x][y] = 1
    while q:
        x, y, distance = q.popleft()
        if 0 < matrix[x][y] < size:
            eating.append((x, y, distance))
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if matrix[nx][ny] > size:
                    continue
                q.append((nx, ny, distance + 1))
                visited[nx][ny] = 1


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
size = 2
start_x = start_y = -1
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(N):
    if start_x != -1:
        break
    for j in range(N):
        if matrix[i][j] == 9:
            start_x = i
            start_y = j
            break
matrix[start_x][start_y] = 0
time = 0
cnt = 0
while True:
    eating = []
    bfs(start_x, start_y, 0)
    if not eating:
        break

    if len(eating) >= 2:
        eating.sort(key=lambda x: x[2])
        idx = 0
        for i, j, d in eating:
            if eating[0][2] == d:
                idx += 1
            else:
                break
        eating = eating[:idx]

    if len(eating) >= 2:
        eating.sort(key=lambda x: x[0])
        idx = 0
        for i, j, d in eating:
            if eating[0][0] == i:
                idx += 1
            else:
                break
        eating = eating[:idx]

    if len(eating) >= 2:
        eating.sort(key=lambda x: x[1])
        idx = 0
        for i, j, d in eating:
            if eating[0][1] == j:
                idx += 1
            else:
                break
        eating = eating[:idx]

    start_x, start_y = eating[0][0], eating[0][1]
    time += eating[0][2]
    matrix[start_x][start_y] = 0
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0

print(time)