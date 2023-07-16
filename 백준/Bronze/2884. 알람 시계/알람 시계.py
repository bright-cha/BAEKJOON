h, m = map(int, input().split())

if m - 45 >= 0:
    print(h, m - 45)
elif h == 0:
    print('23', 15+m)
else:
    print(h-1, 15+m)