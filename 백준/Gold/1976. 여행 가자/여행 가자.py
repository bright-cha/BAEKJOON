import sys

input = sys.stdin.readline


def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    elif x < y:
        parents[y] = x
    else:
        parents[x] = y


N = int(input())
flan_city = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
flan = list(map(int, input().split()))

parents = [i for i in range(N + 1)]

for _ in range(2):
    for i in range(N):
        for j in range(i + 1, N):
            if graph[i][j] == 1:
                union(i + 1, j + 1)

for num in flan:
    if parents[num] != min(flan):
        print('NO')
        break
else:
    print('YES')


