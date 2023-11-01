from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    visited = [[float('inf')] * n for _ in range(n)]
    visited[0][0] = 0
    # x, y, total
    q = deque([(0, 0, 0)])

    while q:
        x, y, t = q.popleft()
        if visited[x][y] < t or visited[n - 1][n - 1] <= t:
            continue

        delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] > t:
                # 흰 방인 경우
                if matrix[nx][ny] == 1:
                    visited[nx][ny] = t
                    q.append((nx, ny, t))
                # 검은 방인 경우
                if matrix[nx][ny] == 0:
                    visited[nx][ny] = t + 1
                    q.append((nx, ny, t + 1))

    return visited[n - 1][n - 1]


n = int(input())
matrix = [list(map(int, input().rstrip())) for _ in range(n)]

print(bfs())
