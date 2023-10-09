import sys
input = sys.stdin.readline
def dfs(x, y, direc):
    global cnt
    if cnt >= 1000000:
        return

    if x == size - 1 and y == size - 1:
        cnt += 1
        return

    # 대각선인 경우
    if x + 1 < size and y + 1 < size:
        if matrix[x + 1][y + 1] == 0 and matrix[x + 1][y] == 0 and matrix[x][y + 1] == 0:
            dfs(x + 1, y + 1, 3)

    # 세로인 경우
    if x + 1 < size and (direc == 2 or direc == 3):
        if matrix[x + 1][y] == 0:
            dfs(x + 1, y, 2)

    # 가로인 경우
    if y + 1 < size and (direc == 1 or direc == 3):
        if matrix[x][y + 1] == 0:
            dfs(x, y + 1, 1)
            
            
size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]

cnt = 0
dfs(0, 1, 1)
print(cnt)