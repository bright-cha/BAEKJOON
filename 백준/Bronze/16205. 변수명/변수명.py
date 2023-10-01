import sys


def camel(case1):
    result = []
    flag = 1
    flag2 = 0
    for item in case1:
        if flag2 == 0:
            result.append(item.lower())
            flag2 =1
            continue
        else:
            if flag == 0:
                result.append(item.upper())
                flag = 1
                continue
            if item == '_':
                flag = 0
                continue
            result.append(item)
    return result


def snake(case1):
    result = []
    result.append(case1[0].lower())
    for i in range(len(case1) - 1):
        if case1[i + 1].isupper():
            result.append('_')
            case1[i+1] =case1[i+1].lower()
        result.append(case1[i + 1])
    return result


def pascal(case1):
    result = []
    flag = 1
    for item in case1:
        if flag == 1:
            result.append(item.upper())
            flag = 0
            continue
        if item == '_':
            flag = 1
            continue
        result.append(item)
    return result


caseDic = {'camel': 1, 'snake': 2, 'pascal': 3}

N, case = sys.stdin.readline().split()
N = int(N)
case1 = list(case)
case2 = list(case)
if N == caseDic['snake']:
    print(''.join(camel(case1)))
    print(case)
    print(''.join(pascal(case1)))
elif N == caseDic['camel']:
    print(case)
    print(''.join(snake(case1)))
    print(''.join(pascal(case2)))
elif N == caseDic['pascal']:
    print(''.join(camel(case1)))
    print(''.join(snake(case1)))
    print(case)