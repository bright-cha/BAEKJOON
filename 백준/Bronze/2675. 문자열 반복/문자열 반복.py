t = int(input())
for i in range(t):
    r, s = input().split()
    r = int(r)

    for k in range(len(s)):
        if s[k] == '\\':
            print('\\' * r, end = '')
        else:
            print(s[k] * r, end = '')
    print('')