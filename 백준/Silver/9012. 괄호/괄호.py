T = int(input())
for _ in range(T):
    word = input()

    rst = []
    for i in word:
        rst += i
        if rst[0] == '(' and ')' in rst:
            rst.pop()
            rst.pop()

    if len(rst) == 0:
        print('YES')
    else:
        print('NO')