from collections import deque


def bfs():
    q = deque([])
    q.append((0, 0))
    visited[0][0] = matrix[0][0]

    while q:
        x, y = q.popleft()

        delta = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
        for nx, ny in delta:
            if 0 <= nx < size and 0 <= ny < size:
                if visited[nx][ny] > visited[x][y] + matrix[nx][ny]:
                    visited[nx][ny] = visited[x][y] + matrix[nx][ny]
                    q.append((nx, ny))


tc = 0
while True:
    tc += 1
    size = int(input())
    if size == 0:
        break

    matrix = [list(map(int, input().split())) for _ in range(size)]

    visited = [[1e9] * size for _ in range(size)]

    bfs()  # x, y, cost
    print(f'Problem {tc}:', visited[size - 1][size - 1])