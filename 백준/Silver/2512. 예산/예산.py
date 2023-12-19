import sys
input = sys.stdin.readline


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
        return binary_search(start, mid - 1)
    else:
        return binary_search(mid + 1, end)


N = int(input())
requests = list(map(int, input().split()))
requests.sort()
M = int(input())

print(binary_search(1, requests[-1]))
