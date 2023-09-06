from collections import deque
import sys
sys.setrecursionlimit(100000)


def move(i, j, dir, sec):
    # 시간 1초 증가
    sec += 1

    # 꼬리남기기
    snake.append((i, j))

    # 머리만 이동
    ni, nj = i + di[dir % 4], j + dj[dir % 4]

    # 이동한 머리가 벽이나 몸에 부딪힌다면 시간 반환
    if not (0 <= ni < size and 0 <= nj < size) or (ni, nj) in snake:
        return sec

    # 움직일 시간이라면 방향을 수정한다.
    if moving_snake and int(moving_snake[0][0]) == sec:
        _, d = moving_snake.popleft()
        if d == 'D':
            dir += 1
        else:
            dir -= 1

    # 사과가 있다면 사과 삭제, 없다면 꼬리 삭제
    if matrix[ni][nj] == 1:
        matrix[ni][nj] = 0
    else:
        snake.popleft()

    # 다음 시간 진행
    return move(ni, nj, dir, sec)


# 보드의 크기
size = int(input())
# 보드 생성
matrix = [[0] * size for _ in range(size)]
# 사과의 개수
cnt_apple = int(input())
# 사과 위치
for _ in range(cnt_apple):
    i, j = map(int, input().split())
    matrix[i - 1][j - 1] = 1
# 움직임 횟수
cnt_moving = int(input())
# 움직임 저장
moving_snake = deque([list(input().split()) for _ in range(cnt_moving)])

# 최종 시간
second = 0
# 뱀 길이 = 인덱스의 개수 + 1 / 뱀의 위치는 2로 표시
snake = deque([])
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# 방향설정
direction = 0
print(move(0, 0, direction, second))  # 행, 열, 방향, 시간