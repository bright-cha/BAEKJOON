import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(idx):
    for i in visited[idx]:
        if not parents[i]:
            parents[i] = idx
            dfs(i)


# 노드의 개수
cnt_node = int(input())
# 자식인덱스에 부모 노드 저장할 리스트
parents = [0] * (cnt_node + 1)
# 간선의 수 = 노드의 개수 - 1 만큼 저장
visited = [[] for _ in range(cnt_node + 1)]
for _ in range(cnt_node - 1):
    i, j = map(int, input().split())
    visited[i].append(j)
    visited[j].append(i)

dfs(1)

for idx in range(2, cnt_node + 1):
    print(parents[idx])