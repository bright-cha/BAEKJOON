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


def kruskal():
    if V == 2:
        return 0
    cnt, rst = 0, 0
    for w, f, t in graph:
        if find_set(f) != find_set(t):
            cnt += 1
            rst += w
            union(f, t)
            if cnt == V - 2:
                return rst


V, E = map(int, input().split())

parents = [i for i in range(V + 1)]
graph = []
for _ in range(E):
    f, t, w = map(int, input().split())
    graph.append([w, f, t])

graph.sort()

print(kruskal())

