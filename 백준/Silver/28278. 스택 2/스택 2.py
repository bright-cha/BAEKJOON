import sys
N = int(input())
stack = []
for _ in range(N):
    enter = list(sys.stdin.readline().split())
    if enter[0] == '1':
        stack.append(enter[-1])
    elif enter[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif enter[0] == '3':
        print(len(stack))
    elif enter[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif enter[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)
