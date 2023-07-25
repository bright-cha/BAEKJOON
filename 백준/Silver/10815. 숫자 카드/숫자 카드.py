import sys
input = sys.stdin.readline

n = int(input())
n_num = set(map(int, input().split()))
m = int(input())
m_num = list(map(int, input().split()))

result = []
for i in m_num:
    if i in n_num:
        result.append(1)
    else:
        result.append(0)

print(*result)
