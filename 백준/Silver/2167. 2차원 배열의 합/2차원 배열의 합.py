import sys
input = sys.stdin.readline
row, col = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(row)]
cnt_sum = int(input())
for _ in range(cnt_sum):
    i, j, x, y = map(int, input().split())
    i, j, x, y = i - 1, j - 1, x - 1, y - 1
    sum_v = 0
    for r in range(i, x + 1):
        for c in range(j, y + 1):
            sum_v += matrix[r][c]

    print(sum_v)