import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def dfs(v):
    global idx
    visited[v] = idx
    for i in graph[v]:
        if visited[i] == 0:
            idx += 1
            dfs(i)


V, E, S = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in graph:
    i.sort()

visited = [0] * (V + 1)
idx = 1
dfs(S)

for i in visited[1:]:
    print(i)
