A, a, B, b, P = map(int, input().split())
if A > B:
    A, B = B, A
    a, b = b, a

rst = 'Yes'
if A + B > P:
    if P < B:
        rst = 'No'

    if A > b:
        rst = 'No'

print(rst)