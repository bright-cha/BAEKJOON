def brute_force(idx, start_team, link_team, start_ability, link_ability):
    global min_v
    if idx == N:
        if len(start_team) == len(link_team):
            min_v = min(min_v, abs(start_ability - link_ability))
        return

    if len(start_team) < N // 2:
        next_ability = sum([matrix[idx][i] + matrix[i][idx] for i in start_team])
        brute_force(idx + 1, start_team + [idx], link_team, start_ability + next_ability, link_ability)

    if len(link_team) < N // 2:
        next_ability = sum([matrix[idx][i] + matrix[i][idx] for i in link_team])
        brute_force(idx + 1, start_team, link_team + [idx], start_ability, link_ability + next_ability)


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

min_v = float('Inf')
brute_force(0, [], [], 0, 0)
print(min_v)
