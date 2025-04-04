import sys
input = sys.stdin.readline


def dp():
    rst.append(sum(lst[:K]))
    start = 0
    end = K
    while end < N:
        rst.append(rst[-1] - lst[start] + lst[end])
        start += 1
        end += 1
    return max(rst)


N, K = map(int, input().split())
lst = list(map(int, input().split()))

rst = []

print(dp())
