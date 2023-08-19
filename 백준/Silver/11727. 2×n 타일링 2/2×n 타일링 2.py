n = int(input())
rst = [1, 3]
for i in range(2, n+1):
    rst.append(rst[i-1] + rst[i-2]*2)
print(rst[n-1] % 10007)