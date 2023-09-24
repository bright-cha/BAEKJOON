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


V, E = map(int, input().split())
truth = list(map(int, input().split()))
party = [list(map(int, input().split())) for _ in range(E)]

parents = [i for i in range(V + 1)]

if truth[0] > 0:
    cnt_true = truth[0]
    for i in truth[1:]:
        parents[i] = 0
else:
    cnt_true = 0

for _ in range(2):
    for part in party:
        for i in range(1, part[0]):
            union(part[i], part[i + 1])

ans = 0
for part in party:
    part_num = part[1:]
    for i in part_num:
        if parents[i] == 0:
            break
    else:
        ans += 1

print(ans)