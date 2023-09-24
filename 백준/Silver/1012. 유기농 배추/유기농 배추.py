from collections import deque


def bfs(i, j):
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        delta = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
        for nx, ny in delta:
            if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] == 1:
                q.append((nx, ny))
                matrix[nx][ny] = 0


T = int(input())
for _ in range(T):
    col, row, cnt_cabbage = map(int, input().split())

    matrix = [[0] * col for _ in range(row)]
    for _ in range(cnt_cabbage):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    cnt = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                cnt += 1
                matrix[i][j] = 0
                bfs(i, j)

    print(cnt)
