cnt_button = int(input())
now = [0] + list(map(int, input().split()))
cnt_student = int(input())
info_student = [list(map(int, input().split())) for _ in range(cnt_student)]
for sex, num in info_student:
    if sex == 1:
        for switch in range(1, cnt_button + 1):
            if switch % num == 0:
                if now[switch] == 1:
                    now[switch] = 0
                else:
                    now[switch] = 1
    elif sex == 2:
        change_lst = [num]
        left_num = num - 1
        right_num = num + 1
        if 1 <= left_num <= cnt_button and 1 <= right_num <= cnt_button:
            while now[left_num] == now[right_num]:
                change_lst.append(left_num)
                change_lst.append(right_num)
                left_num -= 1
                right_num += 1
                if 1 <= left_num <= cnt_button and 1 <= right_num <= cnt_button:
                    pass
                else:
                    break
        for i in change_lst:
            if now[i] == 1:
                now[i] = 0
            else:
                now[i] = 1

for i in range(1, cnt_button + 1):
    if i % 20 == 0:
        print(str(now[i]))
    else:
        print(now[i], end=' ')