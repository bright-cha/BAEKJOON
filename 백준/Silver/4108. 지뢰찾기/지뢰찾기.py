while True:
    row, col = map(int, input().split())
    if row == 0 and col == 0:
        break
    matrix = [list(input()) for _ in range(row)]
    di = [0, 0, 0, 1, 1, 1, -1, -1, -1]
    dj = [0, 1, -1, 0, 1, -1, 0, 1, -1]
    for i in range(row):
        for j in range(col):
            if matrix[i][j] != '*':
                cnt = 0
                for k in range(9):
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < row and 0 <= nj < col:
                        if matrix[ni][nj] == '*':
                            cnt += 1
                matrix[i][j] = cnt

    for i in matrix:
        print(''.join(map(str, i)))
