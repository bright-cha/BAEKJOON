while True:
    n = int(input())
    if n == -1:
        break
    lst = []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)

    lst_str = [str(i) for i in lst]
    a = ' + '.join(lst_str)

    if  sum(lst) == n:
        print(f'{n} = {a}')
    else:
        print(f'{n} is NOT perfect.')