board = []
max_board = []
for i in range(9):
    board.append(list(map(int, input().split())))

for i in range(9):
    max_board.append(max(board[i]))

max_num = max(max_board)

print(max_num)
print(max_board.index(max_num) + 1, board[max_board.index(max_num)].index(max_num) + 1)