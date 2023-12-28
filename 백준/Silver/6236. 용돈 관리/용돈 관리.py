N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]
total_money = sum(money)

start, end = min(money), total_money
while start <= end:
    mid = (start + end) // 2
    my_money = mid

    day = 1
    for i in money:
        if my_money < i:
            my_money = mid
            day += 1
        my_money -= i

    if day > M or mid < max(money):
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)