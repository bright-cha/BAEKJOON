import sys
sys.setrecursionlimit(10 ** 7)
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
parents = [i for i in range(N + 1)]

for _ in range(N - 2):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, N + 1):
    if i == parents[i]:
        print(i, end=' ')
