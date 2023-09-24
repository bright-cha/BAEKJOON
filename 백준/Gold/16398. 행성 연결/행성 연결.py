import sys
input = sys.stdin.readline


def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def kruskal():
    cnt, rst = 0, 0
    for w, f, t in edge:
        # if cnt == V - 1:
        #     return rst
        if find_set(f) != find_set(t):
            cnt += 1
            rst += w
            union(f, t)
    return rst


V = int(input())
matrix = [list(map(int, input().split())) for _ in range(V)]
parents = [i for i in range(V)]

edge = []
for i in range(V):
    for j in range(i + 1, V):
        edge.append((matrix[i][j], i, j))
edge.sort()

print(kruskal())