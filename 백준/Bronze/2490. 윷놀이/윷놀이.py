temp = [list(map(int, input().split())) for _ in range(3)]
for i in temp:
    if i.count(1) == 3:
        print('A')
    if i.count(1) == 2:
        print('B')
    if i.count(1) == 1:
        print('C')
    if i.count(1) == 0:
        print('D')
    if i.count(1) == 4:
        print('E')