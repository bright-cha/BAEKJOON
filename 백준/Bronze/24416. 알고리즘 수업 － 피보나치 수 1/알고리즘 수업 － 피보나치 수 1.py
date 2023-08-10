def fib(n):
    global cnt1
    if n == 1 or n == 2:
        return 1
    else:
        cnt1 += 1
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    global cnt2
    f = [0, 1, 1]
    for i in range(3, n + 1):
        cnt2 += 1
        f.append(f[i - 1] + f[i - 2])
    return f[n]


n = int(input())
cnt1 = 1
cnt2 = 0

print(fibonacci(n), cnt2)