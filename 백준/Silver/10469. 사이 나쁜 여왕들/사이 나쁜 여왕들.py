def check_row(x):  # 남은 로컬의 행과 디큐한 퀸의 좌표가 일치한 경우 False 리턴
    for i in range(7):
        if x == local[i][0]:
            return False
    return True


def check_col(y):  # 남은 로컬의 열과 디큐한 퀸의 좌표가 일치한 경우 False 리턴
    for i in range(7):
        if y == local[i][1]:
            return False
    return True


def check_diagonal(x, y):
    local_possible = []  # 이동가능한 대각선 위치 리스트
    for dx, dy in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        nx, ny = x + dx, y + dy
        while 0 <= nx < 8 and 0 <= ny < 8:
            local_possible.append((nx, ny))
            nx, ny = nx + dx, ny + dy

    for i in local:  # 만약 퀸들의 좌표 중 이동가능한 리스트와 일치하는 경우 False 리턴
        if i in local_possible:
            return False
    return True


def check_solution():  # 유망한지 아닌지 체크
    global row
    if row == 7:     # 종료 조건, row가 7이 될 동안 유지될 경우 True 반환
        return True

    row += 1         # row가 7이 아니라면 1증가
    t = local.pop(0)  # 퀸들의 좌표 중 가장 앞 좌표 디큐
    x, y = t

    if check_row(x) and check_col(y) and check_diagonal(x, y):  # 행, 열, 대각선 공격가능한지 확인
        local.append(t)  # 공격이 불가능할경우 디큐한 좌표 엔큐
        return check_solution()  # 다음 인덱스 체크를 위해 재귀
    else:
        return False  # 공격이 가능한경우 실패 리턴


board = [list(input()) for _ in range(8)]
local = []
# 퀸 좌표 찾기
for i in range(8):
    for j in range(8):
        if board[i][j] == '*':
            local.append((i, j))
            break

# 조사한 인덱스 체크
row = -1
if len(local) == 8:
    if check_solution():
        print('valid')
    else:
        print('invalid')
else:
    print('invalid')