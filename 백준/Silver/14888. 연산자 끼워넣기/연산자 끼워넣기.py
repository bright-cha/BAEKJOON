from collections import deque
import sys
input = sys.stdin.readline


def subset(idx, lens):
    global max_v, min_v
    if idx == lens:
        temp_idx = 0
        num1 = nums[0]
        num2 = 1
        while num2 < cnt_num:
            a1 = num1
            a2 = nums[num2]
            num2 += 1
            oper = operator[temp_idx]
            if oper == '+':
                num1 = a1 + a2
            elif oper == '-':
                num1 = a1 - a2
            elif oper == '*':
                num1 = a1 * a2
            elif oper == '/':
                num1 = abs(a1) // a2
                if a1 < 0:
                    num1 = -num1
            temp_idx += 1
        max_v = max(max_v, num1)
        min_v = min(min_v, num1)
        return
    else:
        for i in range(idx, lens):
            operator[idx], operator[i] = operator[i], operator[idx]
            subset(idx + 1, lens)
            operator[idx], operator[i] = operator[i], operator[idx]


cnt_num = int(input())
nums = list(map(int, input().split()))
operator = deque(list(map(int, input().split())))

for i in '+-*/':
    oper = operator.popleft()
    for _ in range(oper):
        operator.append(i)

max_v = -1e9
min_v = 1e9
subset(0, cnt_num - 1)

print(int(max_v))
print(int(min_v))