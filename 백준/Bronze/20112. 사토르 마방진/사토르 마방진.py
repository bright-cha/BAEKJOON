size = int(input())
matrix = [list(input()) for _ in range(size)]
rst = 1
for i in range(size):
    if rst == 0:
        break
    for j in range(size):
        if i != j and matrix[i][j] != matrix[j][i]:
            rst = 0
            break

if rst:
    print('YES')
else:
    print('NO')