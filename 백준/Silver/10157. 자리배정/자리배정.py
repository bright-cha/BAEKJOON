col, row = map(int, input().split())
wating_num = int(input())

seat = [[0] * col for _ in range(row)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
cnt = 1
i = row - 1
j = 0
k = 0
while cnt < wating_num:
    if row * col < wating_num:
        print(0)
        break
    seat[i][j] = cnt
    ni = i + di[k % 4]
    nj = j + dj[k % 4]
    if 0 <= ni < row and 0 <= nj < col and seat[ni][nj] == 0:
        i = ni
        j = nj
        cnt += 1

    else:
        k += 1
else:
    i = row - i
    print(j + 1, i)