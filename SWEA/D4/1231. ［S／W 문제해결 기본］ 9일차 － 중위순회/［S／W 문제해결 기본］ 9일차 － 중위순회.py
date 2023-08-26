def inorder(idx):
    global rst
    if idx <= size:
        inorder(idx * 2)
        rst += value[idx]
        inorder(idx * 2 + 1)


T = 10
for tc in range(1, T + 1):
    size = int(input())
    edge_info = [list(input().split()) for _ in range(size)]
    rst = ''
    value = [0] * (size + 1)
    ch1 = [0] * (size + 1)
    ch2 = [0] * (size + 1)
    for i in edge_info:
        if len(i) == 4:
            node_num, word, n, m = i
            node_num, n, m = int(node_num), int(n), int(m)
            value[node_num] = word
            ch1 = n
            ch2 = m

        elif len(i) == 3:
            node_num, word, n = i
            node_num, n = int(node_num), int(n)
            value[node_num] = word
            ch1 = n

        else:
            value[int(i[0])] = i[1]

    inorder(1)
    print(f'#{tc}', rst)