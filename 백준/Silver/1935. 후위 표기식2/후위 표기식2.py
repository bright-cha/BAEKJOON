cnt_num = int(input())
operater = list(input())
num = {}
stack = []

for i in operater:
    if i not in '/*-+':
        if cnt_num and i not in num:
            num.setdefault(i, int(input()))
            cnt_num -= 1
        stack.append(num[i])
    else:
        a2 = stack.pop()
        a1 = stack.pop()
        if i == '+':
            stack.append(a1 + a2)
        if i == '-':
            stack.append(a1 - a2)
        if i == '*':
            stack.append(a1 * a2)
        if i == '/':
            stack.append(a1 / a2)

print(f'{stack.pop():.2f}')