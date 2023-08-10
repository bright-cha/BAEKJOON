# 피보나치 재귀함수
def fib(n):
    global cnt1
    if n == 1 or n == 2:
        return 1
    else:
        cnt1 += 1
        return fib(n - 1) + fib(n - 2)

# 피보나치 수열 동적 계획법 / DP / 다이나믹 프로그래밍
def fibonacci(n):
    global cnt2
    f = [0, 1, 1]
    for i in range(3, n + 1):
        cnt2 += 1
        f.append(f[i - 1] + f[i - 2])
    return f[n]


n = int(input())
cnt2 = 0

# 재귀함수 실행 횟수는 피보나치 수만큼 늘어나기에 DP 리턴값을 받고
# 그 실행횟수를 출력한다.
print(fibonacci(n), cnt2)
