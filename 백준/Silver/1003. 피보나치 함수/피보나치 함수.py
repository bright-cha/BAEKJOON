import sys
input = sys.stdin.readline


def fibonacci(num):
    fibo = [(1, 0)] + [(0, 1)] + [[] for _ in range(num)]
    for i in range(2, num + 1):
        fibo[i] = [fibo[i - 1][0] + fibo[i - 2][0], fibo[i - 1][1] + fibo[i - 2][1]]
    return fibo[num]


T = int(input())
for _ in range(T):
    n = int(input())
    print(*fibonacci(n))