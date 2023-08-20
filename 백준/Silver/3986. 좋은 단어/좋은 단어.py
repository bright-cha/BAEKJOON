N = int(input())
cnt = 0
for _ in range(N):
    stack = []
    code = list(input())
    for i in code:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        cnt += 1
print(cnt)
