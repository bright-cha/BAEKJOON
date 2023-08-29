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
            if 1 <= ni < size + 2 and 1 <= nj < size + 2:
                if visited[ni][nj] == 0 and matrix[ni][nj] != 0:
                    que.append((ni, nj))
                    visited[ni][nj] = 1
                    dfs(ni, nj)


size = int(input())
matrix = [[0] * (size + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(size)] + [[0] * (size + 2)]
rst = 0

di = [0, 1]
dj = [1, 0]

visited = [[0] * (size + 2) for _ in range(size + 2)]

que = [(1, 1)]
dfs(1, 1)
if rst == 1:
    print('HaruHaru')
else:
    print('Hing')