def dfs(x, y):
    global rst
    if matrix[x][y] == -1:
        rst = 1
        return
    while que:
        (nx, ny) = que.pop(0)
        for k in range(2):
            g = matrix[nx][ny]
            ni = nx + di[k] * g
            nj = ny + dj[k] * g
            if 0 <= ni < size and 0 <= nj < size:
                if visited[ni][nj] == 0:
                    que.append((ni, nj))
                    visited[ni][nj] = 1
                    dfs(ni, nj)


size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]
rst = 0

di = [0, 1]
dj = [1, 0]

visited = [[0] * size for _ in range(size)]

que = [(0, 0)]
dfs(0, 0)
if rst == 1:
    print('HaruHaru')
else:
    print('Hing')