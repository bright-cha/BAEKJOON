def chack_x():
    global max_v
    val = 0
    for x in range(size):
        for y in range(size):
            dx = x
            while 0 <= dx + 1 < size and board[dx][y] == board[dx + 1][y]:
                val += 1
                dx += 1
            if max_v < val:
                max_v = val
            val = 0


def chack_y():
    global max_v
    val = 0
    for x in range(size):
        for y in range(size):
            dx = x
            while 0 <= dx + 1 < size and board[y][dx] == board[y][dx + 1]:
                val += 1
                dx += 1
            if max_v < val:
                max_v = val
            val = 0


size = int(input())
board = [list(input()) for _ in range(size)]
di, dj = [0, 1], [1, 0]
max_v = 0
for i in range(size):
    for j in range(size):
        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < size and 0 <= nj < size:
                if board[i][j] != board[ni][nj]:
                    board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
                    chack_x()
                    chack_y()
                    board[i][j], board[ni][nj] = board[ni][nj], board[i][j]

print(max_v+1)