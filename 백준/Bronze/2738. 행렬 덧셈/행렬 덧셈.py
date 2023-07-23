n, m = map(int, input().split())

a = []
b = []
for i in range(n):
    a.append([])
    a[i] = list(map(int, input().split()))

for i in range(n):
    b.append([])
    b[i] = list(map(int, input().split()))

result = []
for i in range(n):
    result.append([])
    for j in range(m):
        result[i].append(a[i][j] + b[i][j])
        print(f'{result[i][j]} ', end = '')
    print()