matrix = [[0] * 1001 for _ in range(1001)]
cnt_paper = int(input())
for c in range(1, cnt_paper+1):
    row, col, size1, size2 = map(int, input().split())
    row2, col2 = row + size1 - 1, col + size2 - 1

    for i in range(row, row2 + 1):
        for j in range(col, col2 + 1):
            matrix[i][j] = c

for c in range(1, cnt_paper + 1):
    cnt = 0
    for i in matrix:
        cnt += i.count(c)
    print(cnt)