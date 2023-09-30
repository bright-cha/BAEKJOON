import sys
input = sys.stdin.readline

while 1:
    a, b = input().split()
    if a == b == '0':
        break

    leng = 0
    if len(a) > len(b):
        leng = len(a)
        b = '0' * (len(a) - len(b)) + b
    else:
        leng = len(b)
        a = '0' * (len(b) - len(a)) + a

    cnt = carry = 0
    for i in range(leng-1, -1, -1):
        if (int(a[i]) + int(b[i]) + carry) // 10 == 1:
            cnt += 1
            carry = 1
        else:
            carry = 0

    print(cnt)