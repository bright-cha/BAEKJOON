def enQ(data):
    global rear
    # 원형 큐 사용을 위한 식 생성
    rear = (rear + 1) % 8
    pw[rear] = data


def deQ():
    global front
    # 원형 큐 사용을 위한 식 생성
    front = (front + 1) % 8
    return pw[front]


for tc in range(1, 11):
    T = int(input())
    data = list(map(int, input().split()))
    # 해당문제에서는 포화상태나 빈 상태의 확인이 필요하지 않는다.
    # 모든 공간 활용을 위해 rear와 front를 -1로 변경해도 문제가 생기지 않는다.
    front = -1
    rear = -1

    # 입력받은 data를 모두 큐에 넣는다.
    pw = [0] * 8
    for i in data:
        enQ(i)

    # 감소할 숫자의 크기
    cnt = 1
    while True:
        # 5보다 커질 경우 1로 초기화
        if cnt > 5:
            cnt = 1

        # 가장 먼저 들어간 값을 감소시키고 변수 선언
        # 0보다 작거나 같을 경우 0으로 넣고 큐에 넣고 반복문 종료
        # 0보다 큰 경우 그대로 큐에 넣고 진행한다
        new_n = deQ() - cnt
        if new_n <= 0:
            new_n = 0
            enQ(new_n)
            break
        else:
            enQ(new_n)

        # 감소할 크기 증가
        cnt += 1

    print(f'#{tc}', end=' ')
    for _ in range(8):
        print(deQ(), end=' ')
    print()