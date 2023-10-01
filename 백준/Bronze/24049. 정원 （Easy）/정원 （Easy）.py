N, M = map(int, input().split())
matrix = [[0] * (M + 1) for _ in range(N + 1)]

row = list(map(int, input().split()))
for i in range(1, N + 1):
    matrix[i][0] = row[i - 1]

col = list(map(int, input().split()))
for i in range(1, M + 1):
    matrix[0][i] = col[i - 1]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if matrix[i - 1][j] == matrix[i][j - 1]:
            matrix[i][j] = 0
        else:
            matrix[i][j] = 1

print(matrix[N][M])

