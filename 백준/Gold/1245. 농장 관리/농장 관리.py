from collections import deque


def bfs(i, j):
    global cnt, flag
    que = deque([(i, j)])

    while que:
        i, j = que.popleft()
        for di, dj in dij:
            ni, nj = i + di, j + dj
            if 0 <= ni < row and 0 <= nj < col:
                # 기준점 주위 큰 값이 있다면
                if matrix[i][j] < matrix[ni][nj]:
                    flag = 0
                # 같은 값이있고 방문하지 않았다면
                elif matrix[i][j] == matrix[ni][nj] and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    que.append((ni, nj))
    return


row, col = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(row)]

# 델타 구하기
dij = []
for i in range(-1, 2):
    for j in range(-1, 2):
        if i == 0 and j == 0:
            continue
        dij.append((i, j))

# 하나씩 탐색
cnt = 0
visited = [[0] * col for _ in range(row)]
for i in range(row):
    for j in range(col):
        flag = 1
        # 0이아니고 방문하지않았다면
        if matrix[i][j] != 0 and visited[i][j] == 0:
            bfs(i, j)
            cnt += flag

print(cnt)