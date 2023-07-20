found = list(map(int, input().split()))
perfect = [1, 1, 2, 2, 2, 8]

need = list(map(lambda a, b: a - b, perfect, found))

for i in need:
    print(i, end = " ")
