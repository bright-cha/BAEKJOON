def binary_search(start, end):
    if start > end:
        return end

    mid = (start + end) // 2

    total = 0
    for request in requests:
        if mid > request:
            total += request
        else:
            total += mid

    if total > M:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search(start, end)


# 3 <= N <= 10000
N = int(input())
# 1 <= v <= 100000
requests = list(map(int, input().split()))
requests.sort()
# N <= M <= 1000000000
M = int(input())

if M >= sum(requests):
    print(max(requests))
else:
    print(binary_search(1, requests[-1]))
