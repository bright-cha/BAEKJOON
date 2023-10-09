import sys
input = sys.stdin.readline

size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]
dp = [[[0] * 3 for _ in range(size)] for _ in range(size)] # 0대각선 1 가로 2세로
# 출발 세팅
dp[0][1][1] = 1
# 첫 줄, 0행은 출발지의 가로 상태에서만 이동 가능하니 기록
for i in range(2, size):
    if matrix[0][i] == 0:
        dp[0][i][1] = dp[0][i - 1][1]

for i in range(1, size):
    for j in range(1, size):
        # 이동이 가능한 경우
        if matrix[i][j] == 0:
            # ij의 대각선이 가능한 경우
            if matrix[i][j - 1] == 0 and matrix[i - 1][j] == 0:
                # 꼬리부분 도착 가능 경우 합
                dp[i][j][0] = dp[i - 1][j - 1][0] + dp[i - 1][j - 1][2] + dp[i - 1][j - 1][1]

            # 가로 이동이 가능한 경우
            # 꼬리 부분에서 가로로 이동 가능한 경우 합
            dp[i][j][1] = dp[i][j - 1][0] + dp[i][j - 1][1]
            # 세로 이동이 가능한 경우
            # 꼬리 부분에서 세로로 이동 가능한 경우 합
            dp[i][j][2] = dp[i - 1][j][0] + dp[i - 1][j][2]

# 최종적으로 도착지의 모든 경우의수 합
print(dp[size - 1][size - 1][0] + dp[size - 1][size - 1][1] + dp[size - 1][size - 1][2])