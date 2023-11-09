import sys
input = sys.stdin.readline


for _ in range(int(input().rstrip())):
    W = list(input().rstrip())
    K = int(input().rstrip())

    min_v = 10000
    max_v = 0

    visited = []
    for i in range(len(W) - K + 1):
        if W[i] not in visited:
            count = 0
            for j in range(i, len(W)):
                if W[j] == W[i]:
                    count += 1
                    if count == K:
                        min_v = min(min_v, j - i + 1)
                        max_v = max(max_v, j - i + 1)
                        break
            else:
                visited.append(W[i])

    if min_v == 10000 and max_v == 0:
        print(-1)
    else:
        print(min_v, max_v)
        