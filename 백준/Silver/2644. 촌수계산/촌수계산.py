import sys
sys.setrecursionlimit(10 ** 7)

def dfs(n, t):
    global flag
    if n == a:
        print(t)
        flag = 0
        return
    for i in graph[n]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, t + 1)



V = int(input())
a, b = map(int, input().split())
if a < b:
    a, b = b, a
E = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [0] * (V + 1)
flag = 1
dfs(b, 0)
if flag:
    print(-1)