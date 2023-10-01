size, Z = map(int, input().split())
news = [list(input().split()) if i % Z == 0 else [] for i in range(size * Z)]

for i in range(size * Z):
    for j in range(size):
        if i % Z != 0:
            news[i] = news[i - 1]
        else:
            news[i][j] *= Z

for i in news:
    for j in i:
        print(*j, end=' ')
    print()