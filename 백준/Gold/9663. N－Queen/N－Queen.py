def check_diag(row, col, size, diag_1, diag_2):
    # 대각선 가지치기 함수
    # row와 col을 이용하여 양 대각선에 대한 정보를 확인
    if diag_1[row + col] or diag_2[row - col + size - 1]:
        return False
    return True


def check_candidates(row, size, candidates, used_cols):
    # 열 가지치기 후보 생성 함수
    cnt_candidates = 0
    for col in range(size):
        if not used_cols[col]:
            candidates[cnt_candidates] = col
            cnt_candidates += 1
    return cnt_candidates


def possible_nqeen(row, size, used_cols, diag_1, diag_2):
    global cnt
    candidates = [0] * size
    if row == size:
        cnt += 1
        return

    cnt_candidates = check_candidates(row, size, candidates, used_cols)
    for i in range(cnt_candidates):
        col = candidates[i]
        if check_diag(row, col, size, diag_1, diag_2):
            # 현재 위치가 가능하면 퀸을 배치하고 다음 행으로 이동
            used_cols[col] = True
            diag_1[row + col] = True
            diag_2[row - col + size - 1] = True
            possible_nqeen(row + 1, size, used_cols, diag_1, diag_2)
            # 퀸을 다시 제거하여 백트래킹
            used_cols[col] = False
            diag_1[row + col] = False
            diag_2[row - col + size - 1] = False


size = int(input())
used_cols = [False] * size  # 열 가지치기를 위한 리스트
diag_1 = [False] * (2 * size - 1)  # 대각선 가지치기를 위한 리스트
diag_2 = [False] * (2 * size - 1)  # 대각선 가지치기를 위한 리스트
cnt = 0  # 해의 개수를 저장할 변수

possible_nqeen(0, size, used_cols, diag_1, diag_2)  # 퀸 문제 해결 함수 호출
print(cnt)  # 해의 개수 출력
