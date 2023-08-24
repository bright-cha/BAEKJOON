import sys
input = sys.stdin.readline
def chack():
    global max_v
    for y in range(size):
        val = 0
        dx = 0
        # 각 자리마다 아래칸과 비교하며 내려간다
        while 0 <= dx + 1 < size:
            if board[dx][y] == board[dx + 1][y]:
                val += 1
                dx += 1
            else:
                val = 0
                dx += 1
            if max_v < val:
                max_v = val
        val = 0
        dx = 0
        # 각 자리마다오른칸과 비교하며 내려간다
        while 0 <= dx + 1 < size:
            if board[y][dx] == board[y][dx + 1]:
                val += 1
                dx += 1
            else:
                val = 0
                dx += 1
            if max_v < val:
                max_v = val



size = int(input())
board = [list(input()) for _ in range(size)]
# 아래 오른족 탐색을 위한 델타
di, dj = [0, 1], [1, 0]
# 구할 최대값
max_v = 0
# 모든 자리 확인
for i in range(size):
    for j in range(size):
        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < size and 0 <= nj < size:
                # 내 자리와 변경할 자리가 다른경우
                if board[i][j] != board[ni][nj]:
                    # 변경
                    board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
                    # 확인
                    chack()
                    # 원상복귀
                    board[i][j], board[ni][nj] = board[ni][nj], board[i][j]

print(max_v+1)