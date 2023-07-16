a, b= map(int, input().split())
c = int(input())

d = ((a*60) + b + c)
a = d // 60
if a >= 24:
    a -= 24

b = d % 60

print(a, b)