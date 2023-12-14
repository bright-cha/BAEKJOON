from collections import deque


def bfs(x, y):
    visit[x][y] = False
    q = deque([(x, y)])

    total_people, union = matrix[x][y], [(x, y)]
    while q:
        x, y = q.pop()

        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ni, nj = x + di, y + dj
            if 0 <= ni < N and 0 <= nj < N and visit[ni][nj]:
                # 국경선 공유
                if L <= abs(matrix[x][y] - matrix[ni][nj]) <= R:
                    visit[ni][nj] = False
                    total_people += matrix[ni][nj]
                    union.append((ni, nj))
                    q.append((ni, nj))

    return total_people, union


N, L, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

day = 0

while True:
    record = []
    visit = [[True for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j]:
                total_people, union = bfs(i, j)
                if len(union) > 1:
                    people = total_people // len(union)
                    record.append((people, union))

    for people, country in record:
        for x, y in country:
            matrix[x][y] = people

    if len(record) == 0:
        break

    day += 1

print(day)