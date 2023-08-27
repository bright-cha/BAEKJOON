cnt = 10
board = []
for _ in range(5):
    i = list(map(int, input().split()))
    for j in i:
        board.append(j)

for _ in range(2):
    i = list(map(int, input().split()))
    for j in i:
        board[board.index(j)] = 0

call_num = []
for _ in range(3):
    i = list(map(int, input().split()))
    for j in i:
        call_num.append(j)


while True:
    bingo_line = 0
    if board[0] == 0 and board[6] == 0 and board[12] == 0 and board[18] == 0 and board[24] == 0:
        bingo_line += 1
    if board[4] == 0 and board[8] == 0 and board[12] == 0 and board[16] == 0 and board[20] == 0:
        bingo_line += 1
    for i in range(5):
        if board[0 + i * 5] == 0 and board[1 + i * 5] == 0 and board[2 + i * 5] == 0 and board[3 + i * 5] == 0 and board[4 + i * 5] == 0:
            bingo_line += 1
        if board[0 + i] == 0 and board[5 + i] == 0 and board[10 + i] == 0 and board[15 + i] == 0 and board[20 + i] == 0:
            bingo_line += 1
    if bingo_line >= 3:
        break
    cnt += 1
    next_num = call_num.pop(0)
    board[board.index(next_num)] = 0

print(cnt)
