def bfs(n):
    visited = [0] * (V + 1)
    q = [n]
    while q:
        n = q.pop(0)
        if visited[n] == 0:
            print(n, end=' ')
            visited[n] = 1

        for i in graph[n]:
            if visited[i] == 0:
                q.append(i)


def dfs(n):
    visited[n] = 1
    print(n, end=' ')
    for i in graph[n]:
        if visited[i] == 0:
            dfs(i)


V, E, S = map(int, input().split())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(1, V + 1):
    graph[i].sort()

visited = [0] * (V + 1)
dfs(S)
print()

bfs(S)
