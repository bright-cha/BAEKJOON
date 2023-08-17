import sys
input = sys.stdin.readline

def enq(data):
    global rear
    # 원형 큐 사용을 위한 식 생성
    rear += 1
    wating[rear] = data


def deq():
    global front
    # 원형 큐 사용을 위한 식 생성
    front += 1
    return wating[front]


n = int(input().strip())
# 학식 대기줄
wating = [0] * n

# 최고 줄 길이와 최저 학생의 번호 기록
record = [0, 1e9]

rear = -1
front = -1
for _ in range(n):
    info = list(map(int, input().strip().split()))

    # 정보 유형 1
    if info[0] == 1:
        # 대기줄에 학생 번호 추가
        enq(info[-1])
        # 만약 대기인원이 기록된 최고 줄길이보다 길거나 같다면
        if (rear - front) > record[0]:
            record[1] = 1e9
            # 줄길이 수정
            record[0] = rear - front
            # 기록된 학생 번호보다 새로운 학생의 번호가 작다면 수정
            if record[1] > info[-1]:
                record[1] = info[-1]
        elif (rear - front) == record[0]:
            if record[1] > info[-1]:
                record[1] = info[-1]

    # 정보 유형 2
    else:
        deq()

if record[0] == 0:
    print(0, 0)
else:
    print(*record)