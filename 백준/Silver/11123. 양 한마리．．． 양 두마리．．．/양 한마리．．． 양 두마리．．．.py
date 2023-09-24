from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        delta = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
        for nx, ny in delta:
            if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] == '#':
                q.append((nx, ny))
                matrix[nx][ny] = '.'


T = int(input())
for _ in range(T):
    row, col = map(int, input().split())

    matrix = [list(input()) for _ in range(row)]

    cnt = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == '#':
                cnt += 1
                matrix[i][j] = '.'
                bfs(i, j)

    print(cnt)
