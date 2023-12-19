import heapq


def bfs():
    q = []
    heapq.heappush(q, (0, 0, 0))
    visit[0][0] = 0

    while q:
        cnt, x, y = heapq.heappop(q)

        if visit[x][y] < cnt:
            continue

        if x == N - 1 and y == M - 1:
            return cnt

        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] > cnt + matrix[nx][ny]:
                # 빈 방
                if matrix[nx][ny] == 0:
                    visit[nx][ny] = cnt
                    heapq.heappush(q, (visit[nx][ny], nx, ny))
                    
                # 벽
                else:
                    visit[nx][ny] = cnt + 1
                    heapq.heappush(q, (visit[nx][ny], nx, ny))


M, N = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
visit = [[10000] * M for _ in range(N)]

print(bfs())
