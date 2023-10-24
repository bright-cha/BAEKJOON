from collections import deque

def bfs(n, graph):
    visited = [0] * (n + 1)
    q = deque([1])
    visited[1] = 1
    while q:
        start = q.popleft()
        
        for i in graph[start]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = max(visited) + 1
                
    a = max(visited)
    b = n - a
    return abs(a - b)
    


def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
    
    min_v = 1e9
    for s, e in wires:
        graph[s].remove(e)
        graph[e].remove(s)
        v = bfs(n, graph)
        min_v = min(min_v, v)
        graph[s].append(e)
        graph[e].append(s)
        
    answer = min_v
    return answer