num = int(input())
num_list = [i for i in range(num * 2) if i % 2 == 1]
reverse_num_list = num_list[::-1]

for line in range(2*num - 1):
    if line < num:
        print(' '*(num-line-1) + '*'*num_list[line]) 
    else:
        print(' '*(line-num+1) + '*'*reverse_num_list[abs(num - line) + 1])