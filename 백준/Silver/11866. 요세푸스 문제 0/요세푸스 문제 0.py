def enq(data, arr):
    global rear
    arr[rear] = data
    rear += 1


def deq():
    global front
    front = (front + K-1) % len(lst)
    return lst[front]


N, K = map(int, input().split())
lst = [i for i in range(1, N + 1)]

rear = front = 0
stack = [0] * N

for _ in range(N):
    enq(deq(), stack)
    lst.pop(front)

print('<', end='')
print(', '.join(map(str, stack)), end='')
print('>')