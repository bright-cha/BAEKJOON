import heapq, sys


def dijkstra(red_x, red_y, blue_x, blue_y):
    q = []
    heapq.heappush(q, (0, red_x, red_y, blue_x, blue_y))

    while q:
        cnt, red_x, red_y, blue_x, blue_y = heapq.heappop(q)

        if (red_x, red_y, blue_x, blue_y) in record:
            continue
        else:
            record.append((red_x, red_y, blue_x, blue_y))

        if cnt == 10:
            return -1

        if matrix[blue_x][blue_y] == 'O':
            continue

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            answer = False
            while True:
                nrx, nry = dx + red_x, dy + red_y

                if 0 <= nrx < N and 0 <= nry < M:
                    if matrix[nrx][nry] == '.' and (nrx != blue_x or nry != blue_y):
                        red_x, red_y = nrx, nry
                        continue
                    else:
                        # 성공
                        if matrix[nrx][nry] == 'O':
                            red_x, red_y = nrx + dx, nry + dy
                            answer = True
                break

            while True:
                bnx, bny = dx + blue_x, dy + blue_y

                if 0 <= bnx < N and 0 <= bny < M:
                    if matrix[bnx][bny] == '.' and (red_x != bnx or red_y != bny):
                        blue_x, blue_y = bnx, bny
                        continue
                    else:
                        if matrix[bnx][bny] == 'O':
                            blue_x, blue_y = bnx, bny
                break

            while True:
                nrx, nry = dx + red_x, dy + red_y

                if 0 <= nrx < N and 0 <= nry < M:
                    if matrix[nrx][nry] == '.' and (nrx != blue_x or nry != blue_y):
                        red_x, red_y = nrx, nry
                        continue
                    else:
                        # 성공
                        if matrix[nrx][nry] == 'O':
                            answer = True
                break

            if answer and matrix[blue_x][blue_y] != 'O':
                return cnt + 1

            if record[-1] != (red_x, red_y, blue_x, blue_y):
                heapq.heappush(q, (cnt + 1, red_x, red_y, blue_x, blue_y))

            red_x, red_y, blue_x, blue_y = record[-1]

    return -1


N, M = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
record = []

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'R':
            rx, ry = i, j
            matrix[i][j] = '.'
        if matrix[i][j] == 'B':
            bx, by = i, j
            matrix[i][j] = '.'

print(dijkstra(rx, ry, bx, by))
