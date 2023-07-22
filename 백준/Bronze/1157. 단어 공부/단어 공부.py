a = input().lower()
a_d = {i:0 for i in a}

for i in a:
    if i in a_d:
        a_d[i] = a_d[i] + 1

result = [k for k, v in a_d.items() if v == max(a_d.values())]

if len(result) >= 2:
    print('?')
else:
    print(result[0].upper())
