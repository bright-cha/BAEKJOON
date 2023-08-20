def enq(data):
    global rear
    q[rear] = data
    rear += 1


def deq():
    global front
    front = (front + K-1) % (len(lst))
    return lst[front]



N, K = map(int, input().split())
lst = [i for i in range(1, N + 1)]
q = [0] * N
front = rear = 0
for _ in range(N):
    enq(deq())
    lst.pop(front)

print('<', end='')
print(', '.join(map(str, q)), end='')
print('>')