stack = [0] * 100
top = -1
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
susik = ''
fx = input()
for x in fx:
    # 피연산자의 경우
    if x not in '(+-*/)':  # 피연산자
        susik += x

    # 닫는 괄호의 경우
    elif x == ')':         # '(' 까지 pop()
        while stack[top] != '(':  # peek
            susik += stack[top]
            top -= 1
        top -= 1                  # '(' 버림. pop

    # 연산자의 경우
    else:
        # top이 -1이보다 크고 i 보다 top의 우선순위가 크거나 같다면 pop을 해준다.
        # top이 -1이거나 i의 우선순위가 높아지면 while은 무시되고 pop을 진행한다.
        while top > -1 and isp[stack[top]] >= icp[x]:
            susik += stack[top]
            top -= 1
        top += 1
        stack[top] = x
while top != -1:
    susik += stack[top]
    top -= 1
print(susik)