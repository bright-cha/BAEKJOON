

def solution(park, routes):
    row, col = 0, 0
    x, y = 0, 0
    idx_x = -1
    for i in park:
        idx_x += 1
        idx_y = -1
        row = max(row, idx_x)
        for j in i:
            idx_y += 1
            col = max(col, idx_y)
            if j == 'S':
                x, y = idx_x, idx_y
                break
    for rout in routes:
        direction, distance = rout.split()
        distance = int(distance)
        delta = {
            'N': (-1, 0),
            'S': (1, 0),
            'W': (0, -1),
            'E': (0, 1),
        }
        dx, dy = delta[direction]
        nx, ny = x, y
        for _ in range(distance):
            nx, ny = nx + dx, ny + dy
            if 0 <= nx <= row and 0 <= ny <= col and park[nx][ny] != 'X':
                continue
            else:
                break
        else:
            x, y = nx, ny
    answer = [x, y]
    return answer