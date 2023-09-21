def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


V, E = map(int, input().split())

edge = []
for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append((w, f - 1, t - 1))

edge.sort()

parents = [i for i in range(V)]

cnt, rst = 0, 0
for w, f, t in edge:
    if find_set(f) != find_set(t):
        cnt += 1
        rst += w
        union(f, t)
        if cnt == V:
            break

print(rst)