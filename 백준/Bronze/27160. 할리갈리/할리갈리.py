n = int(input())

fruits = {}
for __ in range(n):
    fruit, num = input().split()
    num = int(num)
    fruits.setdefault(fruit, 0)
    fruits[fruit] = fruits[fruit] + num

if 5 in list(fruits.values()):
    print('YES')
else:
    print('NO')
