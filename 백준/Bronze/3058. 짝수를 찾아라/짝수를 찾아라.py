T = int(input())
for _ in range(T):
    temp = []
    lst = list(map(int, input().split()))
    for i in lst:
        if i % 2 == 0:
            temp.append(i)
    temp.sort()
    print(sum(temp), end=' ')
    print(temp[0])
    