import sys


def check_row(x):
    smooth = 1
    for i in range(1, N):
        if smooth < 0:
            # 다음칸과 같은 경우
            if matrix[x][i - 1] == matrix[x][i]:
                smooth += 1
            else:
                return False
        else:
            # 다음칸과 같은 경우
            if matrix[x][i - 1] == matrix[x][i]:
                smooth += 1

            # 다음 칸이 높은 경우
            elif matrix[x][i - 1] - matrix[x][i] == -1:
                if smooth >= L:
                    smooth = 1
                else:
                    return False

            # 다음 칸이 낮은 경우
            elif matrix[x][i - 1] - matrix[x][i] == 1:
                smooth = -L + 1

            # 그 외 (높이 차가 2 이상인 경우)
            else:
                return False

    if smooth < 0:
        return False
    else:
        return True


def check_col(x):
    smooth = 1
    for i in range(1, N):
        if smooth < 0:
            # 다음칸과 같은 경우
            if matrix[i - 1][x] == matrix[i][x]:
                smooth += 1
            else:
                return False
        else:
            # 다음칸과 같은 경우
            if matrix[i - 1][x] == matrix[i][x]:
                smooth += 1

            # 다음 칸이 높은 경우
            elif matrix[i - 1][x] - matrix[i][x] == -1:
                if smooth >= L:
                    smooth = 1
                else:
                    return False

            # 다음 칸이 낮은 경우
            elif matrix[i - 1][x] - matrix[i][x] == 1:
                smooth = -L + 1

            # 그 외 (높이 차가 2 이상인 경우)
            else:
                return False

    if smooth < 0:
        return False
    else:
        return True


N, L = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    if check_row(i):
        cnt += 1
    if check_col(i):
        cnt += 1

print(cnt)
