while True:
    col, row = map(int, input().split())
    if col == 0 and row == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(row)]

    di = [0, 0, 1, 1, 1, -1, -1, -1]
    dj = [1, -1, 0, 1, -1, 0, 1, -1]
    cnt = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                stack = [(i, j), (i, j)]
                matrix[i][j] = 0
                while stack:
                    for k in range(8):
                        ni, nj = i + di[k], j + dj[k]
                        if 0 <= ni < row and 0 <= nj < col:
                            if matrix[ni][nj] == 1:
                                stack.append((i, j))
                                matrix[ni][nj] = 0
                                i = ni
                                j = nj
                                break
                    else:
                        i, j = stack.pop()
                cnt += 1
    print(cnt)