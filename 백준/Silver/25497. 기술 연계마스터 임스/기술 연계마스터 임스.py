import sys
input = sys.stdin.readline
N = int(input().strip())
skill = list(input().strip())
q = []
cnt = 0
for i in skill:
    if i not in 'SKLR':
        cnt += 1
    else:
        if i == 'R':
            if q and 'L' in q:
                cnt += 1
                q.remove('L')
            else:
                break
        elif i == 'K':
            if q and 'S' in q:
                cnt += 1
                q.remove('S')
            else:
                break
        else:
            q.append(i)
print(cnt)