import sys
input = sys.stdin.readline


def brute_force(idx, start):
    global min_v

    if idx == N // 2:
        link = list(set(i for i in range(N)) - set(start))

        link_ability, start_ability = 0, 0
        for i in range(idx):
            for j in range(idx):
                if i != j:
                    link_ability += matrix[link[i]][link[j]]
                    start_ability += matrix[start[i]][start[j]]

        min_v = min(min_v, abs(start_ability - link_ability))

    else:
        for i in range(start[-1] + 1, N):
            if visited[i]:
                visited[i] = 0
                brute_force(idx + 1, start + [i])
                visited[i] = 1


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [1] * N

min_v = float('Inf')
brute_force(1, [0])
print(min_v)