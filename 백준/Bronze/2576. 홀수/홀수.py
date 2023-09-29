lst = [int(input()) for _ in range(7)]
stack = []
for i in lst:
    if i % 2 == 1:
        stack.append(i)

stack.sort()
if stack:
    print(sum(stack))
    print(stack[0])
else:
    print(-1)