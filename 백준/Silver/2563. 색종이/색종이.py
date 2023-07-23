board = []
for i in range(100):
    board.append([])
    for j in range(100):
        board[i].append(0)

n = int(input())

result = 0
for i in range(n):
    x, y = map(int, input().split())
    for a in range(x, x + 10):
        for b in range(y, y + 10):
            if board[a][b] == 0:
                board[a][b] = 1
                result += 1

print(result)