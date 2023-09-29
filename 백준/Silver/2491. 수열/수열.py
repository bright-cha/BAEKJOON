import sys
input = sys.stdin.readline


N = int(input())
lst = list(map(int, input().split()))

dp1, dp2 = [1] * N, [1] * N
for i in range(1, N):
    # 증감 확인
    idx = lst[i - 1] - lst[i]
    # 만약 증가라면
    if idx >= 0:
        # 이전에 기록된 길이 + 1을 해준다 / 어차피 증가가 이어지지 않는다면 도중에 1로 자동 초기화 된다.
        dp1[i] = dp1[i - 1] + 1
    # 만약 감소라면
    if idx <= 0:
        dp2[i] = dp2[i - 1] + 1

print(max(max(dp1), max(dp2)))